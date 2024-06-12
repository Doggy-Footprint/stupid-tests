from flask import session, request
#reason to use request instead of g is that g should be preprocessed in before request and thus VisitorPermissionChecker depends on outside logic to function
from template_methods import teme_PermissionChecker
from orm_stub import *
from uuid_storage_stub import *

class LoginPermissionChecker(teme_PermissionChecker):
    def check_required(self):
        if not "logged_in" in session: return False
        else:
            if session.get('user_name') == request.args.get('information_owner'): return True
        return False
    def check_sufficient(self):
        return False

class VisitorPermissionChecker(teme_PermissionChecker):
    def check_required(self):
        if not 'logged_in' in session: return False
        if request.args.get('journal_user') == session.get('user_name'): return True
        journal_user_group = find_user_by_name(request.args.get('journal_user')).group
        session_user_group = find_user_by_name(session.get('user_name')).group
        if not journal_user_group is None and not session_user_group is None:
            if journal_user_group.name == session_user_group.name: 
                return True
        else: return False
    def check_sufficient(self):
        if 'temp_permission' in session:
            del session['temp_permission']
            return True
        else: return False

class CardPermissionChecker(teme_PermissionChecker):
    card_permission_uuid_storage = UUIDStorage()
    @classmethod
    def get_card_permission_checker(cls, current_proc):
        uuid_ = session.get('card_uuid')
        user_name = session.get('user_name')
        if current_proc == 'start' \
            and uuid_ is None \
            and session.get('logged_in')\
            and user_name:
            """
            This is for security but not sure it's a good practice to check. 
            Question is,
                1. Is there possibility for another mistake caused from this?
                2. Does this have noticible effect on security?
            """
            new_inst = CardPermissionChecker(user_name)
            uuid_ = cls.card_permission_uuid_storage.put_item_in_storage(new_inst)
            session['card_uuid'] = uuid_
            return new_inst
        card_permission_checker = cls.card_permission_uuid_storage.get_item_by_uuid(uuid_)
        #None / False which should this cls function returns? is there logical answer?
        if card_permission_checker is None: return False
        card_permission_checker.set_current_proc(current_proc)
        return card_permission_checker
    def __init__(self, user_name):
        self.procedure = iter(('start', 'requesting', 'response', 'finished'))
        self.current_proc = 'start'
        self.user_name = user_name
    def set_current_proc(self, current_proc):
        self.current_proc = current_proc
    def check_required(self):
        if next(self.procedure) != self.current_proc: return False
        if not 'logged_in' in session: return False
        if session.get('user_name') != self.user_name: return False
        return True
    def check_sufficient(self):
        return False