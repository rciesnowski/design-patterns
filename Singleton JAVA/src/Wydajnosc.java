import java.io.Serializable;
import java.util.concurrent.atomic.AtomicInteger;
import static org.junit.jupiter.api.Assertions.assertSame;

// 1. Odporność na współbieżne wykorzystanie kodu z jednoczesnym zachowaniem maksymalnej wydajności

enum EnumSingleton {
    INSTANCE
}
class WrappedSingleton {
    private WrappedSingleton(){}
    private static class Wrapper {
        private static final WrappedSingleton inst = new WrappedSingleton();
    }
    public static WrappedSingleton getInstance(){
        return Wrapper.inst;
    }
}
class SingletonBezWartosci implements Serializable {
    SingletonBezWartosci(){}
    private static SingletonBezWartosci single;
    public static SingletonBezWartosci getInstance(){
        SingletonBezWartosci result = single;
        if (result != null) {
            return result;
        }
        synchronized(SingletonBezWartosci.class) {
            if (single == null) single = new SingletonBezWartosci();
            return single;
        }
    }
}

class MultiTest {
    public static final int THREAD_COUNT = 1000;
    public void trying(AtomicInteger count, Object[] singleton) {
        try { Thread.sleep(10); } catch(InterruptedException ignored) {}
        while(count.get() >= 1) {
            try { Thread.sleep(10); } catch(InterruptedException ignored) {}
        }
        for(int i=0;i<THREAD_COUNT - 1;i++) {
            System.out.println(">porownanie watkow " + i + " z " + (i + 1) + ":\n\t" + singleton[i] + "\n\t" + singleton[i + 1]);
            assertSame(singleton[i], singleton[i + 1]);
        }
    }
    @org.junit.jupiter.api.Test
    public void enumTesting(){
        final EnumSingleton[] singleton = new EnumSingleton[THREAD_COUNT];
        final AtomicInteger count = new AtomicInteger(THREAD_COUNT);
        for(int i=0; i < THREAD_COUNT; i++){
            final int l = i;
            new Thread(() -> {
                singleton[l] = EnumSingleton.INSTANCE;
                count.decrementAndGet();
            }).start();
        }
        trying(count, singleton);
    }
    @org.junit.jupiter.api.Test
    public void wrappedTesting(){
        final WrappedSingleton[] singleton = new WrappedSingleton[THREAD_COUNT];
        final AtomicInteger count = new AtomicInteger(THREAD_COUNT);
        for(int i=0; i < THREAD_COUNT; i++){
            final int l = i;
            new Thread(() -> {
                singleton[l] = WrappedSingleton.getInstance();
                count.decrementAndGet();
            }).start();
        }
        trying(count, singleton);
    }
    @org.junit.jupiter.api.Test
    public void singletonTesting() {
        final SingletonBezWartosci[] singleton = new SingletonBezWartosci[THREAD_COUNT];
        final AtomicInteger count = new AtomicInteger(THREAD_COUNT);
        for (int i = 0; i < THREAD_COUNT; i++) {
            final int l = i;
            new Thread(() -> {
                singleton[l] = SingletonBezWartosci.getInstance();
                count.decrementAndGet();
            }).start();
        }
        trying(count, singleton);
    }
}

public class Wydajnosc {
    public static void main(String[] args) {
        long start1 = System.nanoTime();
        for (int i = 0; i<100000; i++) {
            WrappedSingleton.getInstance();
        }
        long end1 = System.nanoTime();
        System.out.println(">sredni czas dla implemetacji 1:\n\t" + (end1 - start1)/100000);
        start1 = System.nanoTime();
        for (int i = 0; i<100000; i++) {
            EnumSingleton instance = EnumSingleton.INSTANCE;
        }
        end1 = System.nanoTime();
        System.out.println(">sredni czas dla implementacji 2 (enum):\n\t" + (end1 - start1)/100000);
        start1 = System.nanoTime();
        for (int i = 0; i<100000; i++) {
            SingletonBezWartosci.getInstance();
        }
        end1 = System.nanoTime();
        System.out.println(">sredni czas dla implementacji 3:\n\t" + (end1 - start1)/100000);
    }
}