package com.example.bywms.client;

import com.example.bywms.model.Features;
import com.example.bywms.model.PredictionResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import java.time.Duration;

@Service
public class PredictionClient {

    private final WebClient webClient;

    public PredictionClient(@Value("${ml.baseUrl:http://localhost:8000}") String baseUrl) {
        this.webClient = WebClient.builder()
                .baseUrl(baseUrl)
                .build();
    }

    public Mono<PredictionResponse> predict(Features f) {
        return webClient.post()
                .uri("/predict")
                .contentType(MediaType.APPLICATION_JSON)
                .bodyValue(f)
                .retrieve()
                .bodyToMono(PredictionResponse.class)
                .timeout(Duration.ofSeconds(3))
                .onErrorReturn(new PredictionResponse(5.0));
    }
}
