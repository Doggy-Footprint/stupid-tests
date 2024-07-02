package dev.devs;

import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.CountDownLatch;
import java.util.Random;

public class VIrtualThread {
    public static void main(String[] args) throws InterruptedException {
        ExecutorService platformThreadPool1 = Executors.newSingleThreadExecutor();
        ExecutorService platformThreadPool2 = Executors.newSingleThreadExecutor();

        CountDownLatch latch = new CountDownLatch(3); // We have three threads to wait for
        Random random = new Random();

        Runnable task = () -> {
            int localValue = 0; // Each task operates on its own local variable
            long tid = Thread.currentThread().getId();
            String tname = Thread.currentThread().getName();

            for (int i = 0; i < 20; i++) { // Increase iterations for better observation
                if (random.nextBoolean()) {
                    int value = random.nextInt(10) + 1;
                    localValue += value;
                    System.out.println(Thread.currentThread().getName() + " added " + value + ", localValue: " + localValue);
                } else {
                    int value = random.nextInt(10) + 1;
                    localValue -= value;
                    System.out.println(Thread.currentThread().getName() + " subtracted " + value + ", localValue: " + localValue);
                }
                try {
                    Thread.sleep(200); // Increase sleep duration to make it easier to observe
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
            latch.countDown(); // Signal that this thread has completed
        };

        // Use a virtual thread per task executor
        ExecutorService virtualThreadExecutor = Executors.newVirtualThreadPerTaskExecutor();

        // Submit tasks to the virtual thread executor
        platformThreadPool1.submit(() -> {
            virtualThreadExecutor.submit(task);
            virtualThreadExecutor.submit(task);
        });

        platformThreadPool2.submit(() -> {
            virtualThreadExecutor.submit(task);
        });

        // Wait for all threads to complete
        latch.await();

        platformThreadPool1.shutdown();
        platformThreadPool2.shutdown();
        virtualThreadExecutor.shutdown();

        System.out.println("All threads have completed their tasks.");
    }
}
