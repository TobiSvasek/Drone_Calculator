# GPS Position Calculator

Tento projekt vypočítává GPS souřadnice dronu v určitém čase během jeho letu pomocí parametrických rovnic.

## Jak skript funguje

1. **Funkce `calculate_gps_position`**:
   - Vstupní parametry: počáteční a koncové GPS souřadnice, celkový čas letu a čas zájmu.
   - Vypočítá směrový vektor přímky (dx, dy).
   - Vypočítá parametr `t` jako podíl času zájmu k celkovému času.
   - Použije parametrické rovnice přímky k výpočtu cílových souřadnic (target_lat, target_lon).
   - Vrátí cílové souřadnice jako tuple (lat, lon).

2. **Funkce `format_coordinates`**:
   - Vstupní parametry: zeměpisná šířka a délka.
   - Určí směrové označení (N/S pro šířku, E/W pro délku).
   - Naformátuje souřadnice do textového formátu s přesností na 7 desetinných míst.
   - Vrátí naformátované souřadnice jako text.

3. **Funkce `main`**:
   - Vyžádá si vstupní hodnoty od uživatele: počáteční a koncové GPS souřadnice, celkový čas letu a čas zájmu.
   - Zavolá funkci `calculate_gps_position` pro výpočet cílových souřadnic.
   - Zavolá funkci `format_coordinates` pro naformátování cílových souřadnic.
   - Vytiskne výsledné GPS souřadnice.

4. **Spuštění skriptu**:
   - Pokud je skript spuštěn jako hlavní program, zavolá funkci `main`.