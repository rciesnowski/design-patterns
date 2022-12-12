//W programie wielowątkowym, konstrukcja zapewniająca jeden singleton na program
import org.junit.jupiter.api.Test;
import java.util.concurrent.atomic.AtomicInteger;
import static org.junit.jupiter.api.Assertions.assertSame;

// 4. W programie wielowątkowym, konstrukcja zapewniająca jeden singleton na wątek
// Przykłady kontrolne:
// singleton naiwny narażony jest na wystąpienie dwóch instancji w tym samym wątku
// singleton z zabezpieczeniem w każdym wątku będzie odwoływał się do tej samej instancji

public class WielowatkowoscTest {
    public static final int CONCURRENT_THREADS = 4;
    private void singleNaiwny() {
        final SingletonNaiwny[] singleton = new SingletonNaiwny[CONCURRENT_THREADS];
        final AtomicInteger count = new AtomicInteger(CONCURRENT_THREADS);
        for(int i=0;i<CONCURRENT_THREADS;i++) {
            final int l = i;
            new Thread(() -> {
                if (l%2 == 0) {
                    singleton[l] = SingletonNaiwny.getInstance();
                } else {
                    singleton[l] = SingletonNaiwny.getInstance("gruszka");
                }
                System.out.println("\t" + singleton[l] + " " + singleton[l].getWartosc());
                count.decrementAndGet();
            }).start();
        }
        trying(singleton, count);
    }
    private void single() {
        final Singleton[] singleton = new Singleton[CONCURRENT_THREADS];
        final AtomicInteger count = new AtomicInteger(CONCURRENT_THREADS);
        for(int i=0;i<CONCURRENT_THREADS;i++) {
            final int l = i;
            new Thread(() -> {
                if (l%2 == 0) {
                    singleton[l] = Singleton.getInstance();
                } else {
                    singleton[l] = Singleton.getInstance("gruszka");
                }
                System.out.println("\t" + singleton[l] + " " + singleton[l].getWartosc());
                count.decrementAndGet();
            }).start();
        }
        trying(singleton, count);
    }

    private void trying(Object[] singleton, AtomicInteger count) {
        try { Thread.sleep(10); } catch(InterruptedException ignored) { }
        while(count.get() >= 1) {
            try { Thread.sleep(10); } catch(InterruptedException ignored) { }
        }
        for(int i=0;i<CONCURRENT_THREADS - 1;i++) {
            assertSame(singleton[i], singleton[i + 1]);
        }
    }

    @Test
    public void testSingletonNaiwny() {
        System.out.println("IMPLEMENTACJA NAIWNA");
        for(int i=0;i<100;i++) {
            System.out.println(">para nr. " + (i+1));
            SingletonNaiwny.single = null;
            singleNaiwny();
        }
    }
    @Test
    public void testSingleton() {
        System.out.println("IMPLEMENTACJA Z ZABEZPIECZENIEM");
        for(int i=0;i<100;i++) {
            System.out.println(">para nr. " + (i+1));
            Singleton.single = null;
            single();
        }
    }
}