package gy8;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import java.util.Map;
import java.util.HashMap;

public class JegyekTeszt {

    @Test
    public void testGetPontszam() {
        Map<String, Integer> jegyek = new HashMap<>();
        jegyek.put("Szabo Peter", 92);
        assertEquals(92, jegyek.get("Szabo Peter"));
    }

    @Test
    public void testIsmeretlenDiak() {
        Map<String, Integer> jegyek = new HashMap<>();
        assertNull(jegyek.get("Ismeretlen Diák"));
    }

    @Test
    public void testAtlagSzamitas() {
        Map<String, Integer> jegyek = new HashMap<>();
        jegyek.put("Kovacs Peter", 85);
        jegyek.put("Nagy Anna", 92);
        jegyek.put("Szabo Bela", 76);
        int osszeg = 85 + 92 + 76;
        double atlag = (double) osszeg / 3;
        assertEquals(84.33, Math.round(atlag * 100.0) / 100.0);
    }
}
