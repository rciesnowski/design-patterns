import java.io.Serializable;

public class SingletonNaiwny implements Serializable {
    SingletonNaiwny(String wartosc) {
        this.wartosc = wartosc;
    }
    SingletonNaiwny() {}
    public static SingletonNaiwny single;
    private String wartosc = "japko";
    public String getWartosc() {
        return wartosc;
    }
    public void setWartosc(String wartosc) {
        this.wartosc = wartosc;
    }
    public static SingletonNaiwny getInstance(String wartosc){
        if (single == null) single = new SingletonNaiwny(wartosc);
        return single;
    }
    public static SingletonNaiwny getInstance(){
        if (single == null) single = new SingletonNaiwny();
        return single;
    }
}
