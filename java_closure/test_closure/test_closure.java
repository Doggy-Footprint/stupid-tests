package test_closure;

/**
 * in java_closure directory
 * javac test_closure/test_closure.java
 * java test_closure.MainClass
 */

interface OneMethodInterface {
    public void run();
}

class MainClass {
    public static void main(String args[]) {
        WorkingClass worker = new WorkingClass();
        worker.work();
        OtherClass.run(worker.impl1, worker.impl2);
    }
}

class WorkingClass {

    private String const_str = "const";

    public OneMethodInterface impl1;
    public OneMethodInterface impl2;

    public void exec(OneMethodInterface interface1, OneMethodInterface impl2) {
        interface1.run();
        impl2.run();
    }

    public void work() {
        OneMethodInterface impl1 = () -> {
            System.out.println("---impl1---");
            this.const_str = this.const_str + " impl1 ";
            System.out.println(this.const_str);
            System.out.println("hashCode of const_str in impl1: " + this.const_str.hashCode());
            return;
        };

        OneMethodInterface impl2 = () -> {
            System.out.println("---impl2---");
            const_str = const_str + " impl2 ";
            System.out.println(const_str);
            System.out.println("hashCode of const_str in impl2: " + this.const_str.hashCode());
            return;
        };
        System.out.println("hashCode of const_str in work: " + this.const_str.hashCode());
        impl1.run();
        impl2.run();
        System.out.println("\nconst_str in work: " + const_str);

        this.impl1 = impl1;
        this.impl2 = impl2;
        return;
    }
}

class OtherClass {
    public static void run(OneMethodInterface interface1, OneMethodInterface impl2) {
        interface1.run();
        impl2.run();
    }
}