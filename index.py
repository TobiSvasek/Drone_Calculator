def calculate_gps_position(start_lat, start_lon, end_lat, end_lon, total_time, time_of_interest):
    """
    Vypočítá GPS souřadnice na trase dronu v čase zájmu.

    Parametry:
    - start_lat: Zeměpisná šířka počátečního bodu.
    - start_lon: Zeměpisná délka počátečního bodu.
    - end_lat: Zeměpisná šířka koncového bodu.
    - end_lon: Zeměpisná délka koncového bodu.
    - total_time: Celkový čas letu (v sekundách).
    - time_of_interest: Čas na videu (v sekundách), kde je potřeba zjistit polohu.

    Návratová hodnota:
    - Tuple (lat, lon): Souřadnice požadovaného bodu.
    """
    # Poměr času zájmu k celkovému času
    k = time_of_interest / total_time

    # Interpolace GPS souřadnic
    target_lat = start_lat + k * (end_lat - start_lat)
    target_lon = start_lon + k * (end_lon - start_lon)

    return target_lat, target_lon


def format_coordinates(lat, lon):
    """
    Naformátuje GPS souřadnice podle standardu se směrovým označením.

    Parametry:
    - lat: Zeměpisná šířka.
    - lon: Zeměpisná délka.

    Návratová hodnota:
    - Formátované souřadnice jako text.
    """
    lat_direction = 'N' if lat >= 0 else 'S'
    lon_direction = 'E' if lon >= 0 else 'W'

    formatted_lat = f"{abs(lat):.7f}{lat_direction}"
    formatted_lon = f"{abs(lon):.7f}{lon_direction}"

    return formatted_lat, formatted_lon


def main():
    print("Zadejte vstupní hodnoty:")
    start_lat = float(input("Počáteční zeměpisná šířka (latitude): "))
    start_lon = float(input("Počáteční zeměpisná délka (longitude): "))
    end_lat = float(input("Koncová zeměpisná šířka (latitude): "))
    end_lon = float(input("Koncová zeměpisná délka (longitude): "))
    total_time = float(input("Celkový čas letu (v sekundách): "))
    time_of_interest = float(input("Čas na videu, kde je místo k údržbě (v sekundách): "))

    # Výpočet GPS polohy
    target_lat, target_lon = calculate_gps_position(
        start_lat, start_lon, end_lat, end_lon, total_time, time_of_interest
    )

    # Formátování souřadnic
    formatted_lat, formatted_lon = format_coordinates(target_lat, target_lon)

    print(f"\nGPS souřadnice místa k údržbě: {formatted_lat}, {formatted_lon}")


if __name__ == "__main__":
    main()
