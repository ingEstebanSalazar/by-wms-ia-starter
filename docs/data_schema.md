# Esquema de Datos · ETA Picking (ejemplo)

**Features sugeridas:**
- `wh_id` (categórica), `aisle`, `zone`, `op_code`
- `distance_est` (float), `sku_volume` (float)
- `wave_size` (int), `weekday` (0-6), `hour` (0-23)
- `picker_experience` (opcional), `congestion_index` (opcional)

**Target:**
- `eta_minutes` (float)

**Calidad de dato:**
- Imputación de nulos (mediana/moda).
- Outliers: winsorizing/p95.
- Encoding: OneHot/Ordinal para categóricas.
