package com.example.weatherappproject

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance {

    // Base URL for OpenWeatherMap API
    private const val BASE_URL = "https://api.openweathermap.org/data/2.5/"

    // Create Retrofit instance and provide the API service
    val api: WeatherApi by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())  // Converter for JSON to Kotlin objects
            .build()
            .create(WeatherApi::class.java)  // The WeatherApi interface to define the API calls
    }
}

