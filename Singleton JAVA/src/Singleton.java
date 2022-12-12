import java.io.ObjectStreamException;
import java.io.Serial;
import java.io.Serializable;

public class Singleton implements Serializable {
    Singleton(String wartosc) {
        this.wartosc = wartosc;
    }
    Singleton() {}
    public static volatile Singleton single;
    private String wartosc = "japko";
    public String getWartosc() {
        return wartosc;
    }
    // do zmiany wartosci
    public void setWartosc(String wartosc) {
        this.wartosc = wartosc;
    }
    // double-locking
    public static Singleton getInstance(String wartosc){
        Singleton result = single;
        if (result != null) {
            return result;
        }
        synchronized(Singleton.class) {
            if (single == null) single = new Singleton(wartosc);
            return single;
        }
    }

    public static Singleton getInstance(){
        Singleton result = single;
        if (result != null) {
            return result;
        }
        synchronized(Singleton.class) {
            if (single == null) single = new Singleton();
            return single;
        }
    }
    // zwraca oryginalnego singletona zamiast tworzyc nowego
    @Serial
    protected Object readResolve() {
        single.setWartosc(getWartosc());
        return single;
    }
}