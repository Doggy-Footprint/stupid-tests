package dev.devs;

import dev.devs.practice.SyncSample;

/**
 * Been a while and funny mistake.
 *
 * result:
 * Test thread safety
 * shared - increment started
 * shared - decrement started
 * shared - increment done 9612
 * shared - decrement done 0
 * shared done
 * -----
 * Test A, B
 * a - increment started
 * b - increment started
 * a - increment done 100000
 * b - increment done 100000
 * AB done
 *
 * The random 'shared - increment done 9612' done value is not matter of thread safety.
 * single increment, and decrement is protected not entire loop.
 * 'shared - decrement done 0' is the proof of thread safety
 */
public class SyncTest {

    public static final int REPEAT = 100000;

    public SyncSample a = new SyncSample();
    public SyncSample b = new SyncSample();
    public SyncSample shared = new SyncSample();


    public static void main(String[] args) {
        SyncTest st = new SyncTest();

        st.testShared();
        System.out.println("-----");
        st.testAB();
    }

    public void testShared() {
        System.out.println("Test thread safety");

        Runnable r1 = new Runnable() {
            @Override
            public void run() {
                boolean once = true;
                for (int i = 0; i < SyncTest.REPEAT; i++) {
                    shared.increment();
                    if (once) {
                        System.out.println("shared - increment started");
                        once = false;
                    }
                }
                System.out.println("shared - increment done " + String.valueOf(shared.value()));
            }
        };

        Runnable r2 = new Runnable() {
            @Override
            public void run() {
                boolean once = true;
                for (int i = 0; i < SyncTest.REPEAT; i++) {
                    shared.decrement();
                    if (once) {
                        System.out.println("shared - decrement started");
                        once = false;
                    }
                }
                System.out.println("shared - decrement done " + String.valueOf(shared.value()));
            }
        };

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        System.out.println("shared done");
    }

    public void testAB() {
        System.out.println("Test A, B");

        Runnable r1 = new Runnable() {
            @Override
            public void run() {
                boolean once = true;
                for (int i = 0; i < SyncTest.REPEAT; i++) {
                    a.increment();
                    if (once) {
                        System.out.println("a - increment started");
                        once = false;
                    }
                }
                System.out.println("a - increment done " + String.valueOf(a.value()));
            }
        };

        Runnable r2 = new Runnable() {
            @Override
            public void run() {
                boolean once = true;
                for (int i = 0; i < SyncTest.REPEAT; i++) {
                    b.increment();
                    if (once) {
                        System.out.println("b - increment started");
                        once = false;
                    }
                }
                System.out.println("b - increment done " + String.valueOf(b.value()));
            }
        };

        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        System.out.println("AB done");
    }
}