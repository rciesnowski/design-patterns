import java.io.*;

// 3. Problem serializacji i deserializacji obiektów klasy Singleton

public class Serializacja {
    public static void serializuj(Singleton single, String plik) throws IOException {
        FileOutputStream fileOut = new FileOutputStream(plik);
        ObjectOutputStream out = new ObjectOutputStream(fileOut);
        out.writeObject(single);
        out.close();
        fileOut.close();
        System.out.println(">zapisano do pliku");
    }
    public static Singleton deserializuj(String plik) throws IOException, ClassNotFoundException {
        FileInputStream fileIn = new FileInputStream(plik);
        ObjectInputStream in = new ObjectInputStream(fileIn);
        Singleton serial = (Singleton) in.readObject();
        in.close();
        fileIn.close();
        System.out.println(">deserializacja");
        return serial;
    }
    public static void serializujN(SingletonNaiwny single, String plik) throws IOException {
        FileOutputStream fileOut = new FileOutputStream(plik);
        ObjectOutputStream out = new ObjectOutputStream(fileOut);
        out.writeObject(single);
        out.close();
        fileOut.close();
        System.out.println(">zapisano do pliku");
    }
    public static SingletonNaiwny deserializujN(String plik) throws IOException, ClassNotFoundException {
        FileInputStream fileIn = new FileInputStream(plik);
        ObjectInputStream in = new ObjectInputStream(fileIn);
        SingletonNaiwny serial = (SingletonNaiwny) in.readObject();
        in.close();
        fileIn.close();
        System.out.println(">deserializacja");
        return serial;
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        System.out.println("IMPLEMENTACJA NAIWNA");
        SingletonNaiwny oryginalN = SingletonNaiwny.getInstance("japko");
        serializujN(oryginalN,"singleton.ser");
        System.out.println(">zmiana wartosci oryginal na gruszke");
        oryginalN.setWartosc("gruszka");
        System.out.println("\toryginal: " + oryginalN.hashCode() + " " + oryginalN.getWartosc());
        SingletonNaiwny serialN = deserializujN("singleton.ser");
        System.out.println("\tserial: " + serialN.hashCode() + " " + serialN.getWartosc());
        System.out.println(">zmieniamy wartosc oryginal na pomarancz");
        oryginalN.setWartosc("pomarancz");
        System.out.println("\tserial: " + serialN.hashCode() + " " + serialN.getWartosc());
        System.out.println(">obiekty sa tozsame?\n\t" + (serialN == oryginalN));

        System.out.println("\nIMPLEMENTACJA Z ZABEZPIECZENIEM");
        Singleton oryginal = Singleton.getInstance("japko");
        serializuj(oryginal,"singleton.ser");
        System.out.println(">zmiana wartosci oryginal na gruszke");
        oryginal.setWartosc("gruszka");
        System.out.println("\toryginal: " + oryginal.hashCode() + " " + oryginal.getWartosc());
        Singleton serial = deserializuj("singleton.ser");
        System.out.println("\tserial: " + serial.hashCode() + " " + serial.getWartosc());
        System.out.println(">zmieniamy wartosc oryginal na pomarancz");
        oryginal.setWartosc("pomarancz");
        System.out.println("\tserial: " + serial.hashCode() + " " + serial.getWartosc());
        System.out.println(">obiekty sa tozsame?\n\t" + (serial == oryginal));
    }
}