package gy8;

import java.util.Map;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Map.Entry;

public class Jegyek{

    private Map<String, Integer> jegyek = new HashMap<>();

    public void DiakokPontjai(){
        System.out.println("Diákok pontszámai:");
        for (Map.Entry<String, Integer> entry : jegyek.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue() + " pont");
        }
    }
    
    public void getDiakPontszam(String nev){
        if(jegyek.containsKey(nev)){
            System.out.println(nev + " pontszama: " + jegyek.get(nev) + " pont!");
        }else{
            System.out.println("Nincs ilyen nevu diak!");
        }
    }

    public double getAtlag(){
        int osszeg = 0;
        for (int pont : jegyek.values()) {
            osszeg += pont;
        }
        double atlag = (double) osszeg / jegyek.size();
        return atlag;
    }
    
}