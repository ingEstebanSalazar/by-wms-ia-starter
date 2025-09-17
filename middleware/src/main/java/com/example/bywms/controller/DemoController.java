package com.example.bywms.controller;

import com.example.bywms.client.PredictionClient;
import com.example.bywms.model.PredictionResponse;
import com.example.bywms.model.Features;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
@RequiredArgsConstructor
public class DemoController {

    private final PredictionClient client;

    @GetMapping("/demo/eta")
    public Mono<PredictionResponse> demo(
            @RequestParam double distance_est,
            @RequestParam double sku_volume,
            @RequestParam int wave_size,
            @RequestParam int weekday,
            @RequestParam int hour) {
        Features f = new Features(distance_est, sku_volume, wave_size, weekday, hour);
        return client.predict(f);
    }
}
