package com.example.bywms.model;

import lombok.*;

@Data @NoArgsConstructor @AllArgsConstructor
public class PredictionResponse {
    private double eta_minutes;
}

@Data @Builder @AllArgsConstructor @NoArgsConstructor
class Features {
    private double distance_est;
    private double sku_volume;
    private int wave_size;
    private int weekday;
    private int hour;
}
