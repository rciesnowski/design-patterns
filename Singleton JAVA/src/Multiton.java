// 4. W programie wielowątkowym, konstrukcja zapewniająca jeden singleton na wątek
// Przykład badawczy:
// W każdym wątku będzie dokładnie jedna instancja singletona

class SingletonLocal {
    private SingletonLocal() {}
    public String getWartosc() { return wartosc; }
    public void setWartosc(String wartosc) { SingletonLocal.wartosc = wartosc; }
    private static String wartosc = "japko";
    private static final java.lang.ThreadLocal<SingletonLocal> _threadLocal = java.lang.ThreadLocal.withInitial(SingletonLocal::new);
    public static SingletonLocal getInstance() { return _threadLocal.get(); }
}

class ThreadLocal extends Thread {
    public void run() {
        SingletonLocal instance1 = SingletonLocal.getInstance();
        System.out.println(">" + Thread.currentThread().getName() + "\n\t" + instance1 + " " + instance1.getWartosc());
        try {
            Thread.sleep(10);
        } catch (InterruptedException ignored) {}
        SingletonLocal instance2 = SingletonLocal.getInstance();
        instance1.setWartosc("gruszka");
        System.out.println(">" + Thread.currentThread().getName() + " po zmianie wartosci pierwszej instancji:\n\t" + instance2 + " " + instance2.getWartosc());
    }
}

public class Multiton {
    public static void main(String[] args) {
        Thread jedynka = new ThreadLocal();
        Thread dwojka = new ThreadLocal();
        jedynka.start();
        dwojka.start();
    }
}