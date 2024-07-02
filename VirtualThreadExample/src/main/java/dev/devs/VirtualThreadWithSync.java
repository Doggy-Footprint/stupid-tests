package dev.devs;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.CountDownLatch;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class VirtualThreadWithSync {

    private static final List<Integer> sharedList = new ArrayList<>();
    private static final Random random = new Random();

    public static void main(String[] args) throws InterruptedException {
        ExecutorService platformThreadPool1 = Executors.newSingleThreadExecutor();
        ExecutorService platformThreadPool2 = Executors.newSingleThreadExecutor();

        CountDownLatch latch = new CountDownLatch(3); // We have three threads to wait for

        Runnable task = () -> {
            for (int i = 0; i < 20; i++) { // Increase iterations for better observation
                synchronized (sharedList) {
                    if (random.nextBoolean()) {
                        int value = random.nextInt(10) + 1;
                        sharedList.add(value);
                        System.out.println(Thread.currentThread().getName() + " added " + value);
                    } else if (!sharedList.isEmpty()) {
                        int index = random.nextInt(sharedList.size());
                        int removedValue = sharedList.remove(index);
                        System.out.println(Thread.currentThread().getName() + " removed " + removedValue);
                    }
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