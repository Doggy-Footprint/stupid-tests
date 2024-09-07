package dev.devs.synchronization;

public class SyncSampleLoop {
    private int loop = 1000000;
    private int c = 0;

    public SyncSampleLoop() {}
    public SyncSampleLoop(int loop) {
        this();
        this.loop = loop;
    }

    public synchronized void increase() {
        for (int i = 0; i < this.loop; i++) {
            c++;
        }
    }

    public synchronized void decrease() {
        for (int i = 0; i < this.loop; i++) {
            c--;
        }
    }

    public synchronized int value() {
        return c;
    }
}
