class teme_PermissionChecker:
    def check_required(self):
        raise NotImplementedError("teme_PermissionChecker.check_state must be implemented")
    def check_sufficient(self):
        raise NotImplementedError("teme_PermissionChecker.check_visitor must be implemented")
    def check_permission(self):
        if self.check_sufficient():
            print('check_permission: sufficient condition satisfied')
            return True
        elif self.check_required(): 
            print('check_permission: required condition satisfied')
            return True
        else: return False