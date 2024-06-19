# Closure

Closure는 외부 scope에 접근할 수 있는 함수를 뜻합니다. 이 예시 프로젝트에서 WorkingClass는 `impl1`, `impl2` 두 closure를 만들고, 이 closure는 WorkingClass의 private 변수인 const에 접근하고, 수정할 수 있습니다.

이는 `OneMethodInterface` context에서 한 번 보이고, `OtherClass`에서 `impl1`, `impl2`를 인자로 받아 실행함으로서 WorkingClass 객체의 상태를 변경하는 것으로 또 한 번 보입니다.

