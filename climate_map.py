import openmeteo_requests
import requests_cache
import pandas as pd
import plotly.express as px
from retry_requests import retry

# Setup API client dengan cache
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Kota-kota besar Indonesia beserta koordinatnya
cities = {
    "Banda Aceh":     (5.5477, 95.3238),
    "Medan":          (3.5952, 98.6722),
    "Padang":         (-0.9471, 100.4172),
    "Pekanbaru":      (0.5071, 101.4478),
    "Palembang":      (-2.9761, 104.7754),
    "Bandar Lampung": (-5.4292, 105.2613),
    "Jakarta":        (-6.2088, 106.8456),
    "Bandung":        (-6.9175, 107.6191),
    "Semarang":       (-6.9932, 110.4203),
    "Yogyakarta":     (-7.7956, 110.3695),
    "Surabaya":       (-7.2504, 112.7688),
    "Denpasar":       (-8.6705, 115.2126),
    "Mataram":        (-8.5833, 116.1167),
    "Kupang":         (-10.1772, 123.6070),
    "Pontianak":      (0.0263, 109.3425),
    "Palangkaraya":   (-2.2136, 113.9108),
    "Banjarmasin":    (-3.3194, 114.5908),
    "Samarinda":      (-0.5016, 117.1537),
    "Makassar":       (-5.1477, 119.4327),
    "Palu":           (-0.9003, 119.8779),
    "Kendari":        (-3.9985, 122.5129),
    "Manado":         (1.4748, 124.8421),
    "Gorontalo":      (0.5435, 123.0568),
    "Ambon":          (-3.6954, 128.1814),
    "Jayapura":       (-2.5337, 140.7181),
    "Sorong":         (-0.8833, 131.2500),
    "Manokwari":      (-0.8615, 134.0754),
}

print("🌏 Mengambil data iklim dari Open-Meteo...")

results = []
for city, (lat, lon) in cities.items():
    try:
        response = openmeteo.weather_api(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
                "timezone": "Asia/Jakarta",
                "forecast_days": 7
            }
        )[0]

        daily = response.Daily()
        temp_max = daily.Variables(0).ValuesAsNumpy().mean()
        temp_min = daily.Variables(1).ValuesAsNumpy().mean()
        precip   = daily.Variables(2).ValuesAsNumpy().mean()

        results.append({
            "City": city,
            "Latitude": lat,
            "Longitude": lon,
            "Avg Max Temp (°C)": round(temp_max, 1),
            "Avg Min Temp (°C)": round(temp_min, 1),
            "Avg Precipitation (mm)": round(precip, 1)
        })
        print(f"  ✅ {city}: {temp_max:.1f}°C, {precip:.1f}mm")

    except Exception as e:
        print(f"  ❌ {city}: {e}")

df = pd.DataFrame(results)

# Peta suhu interaktif
fig_temp = px.scatter_map(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Avg Max Temp (°C)",
    size="Avg Max Temp (°C)",
    hover_name="City",
    hover_data=["Avg Max Temp (°C)", "Avg Min Temp (°C)", "Avg Precipitation (mm)"],
    color_continuous_scale="RdYlBu_r",
    zoom=4,
    center={"lat": -2.5, "lon": 118},
    title="🌡️ Indonesia - Average Max Temperature (7-Day Forecast)",
    map_style="carto-positron"
)
fig_temp.write_html("temperature_map.html")
print("\n✅ Peta suhu tersimpan: temperature_map.html")

# Peta curah hujan interaktif
fig_rain = px.scatter_map(
    df,
    lat="Latitude",
    lon="Longitude",
    color="Avg Precipitation (mm)",
    size="Avg Precipitation (mm)",
    hover_name="City",
    hover_data=["Avg Max Temp (°C)", "Avg Min Temp (°C)", "Avg Precipitation (mm)"],
    color_continuous_scale="Blues",
    zoom=4,
    center={"lat": -2.5, "lon": 118},
    title="🌧️ Indonesia - Average Precipitation (7-Day Forecast)",
    map_style="carto-positron",
)
fig_rain.write_html("rainfall_map.html")
print("✅ Peta curah hujan tersimpan: rainfall_map.html")

print("\n🎉 Selesai! Buka temperature_map.html dan rainfall_map.html di browser.")