
package com.example.weatherappproject

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Query

interface WeatherApi {

    // Endpoint for fetching weather data based on city name
    @GET("weather")
    fun getWeather(
        @Query("q") cityName: String,  // City name query
        @Query("appid") apiKey: String  // API key query
    ): Call<WeatherResponse>
}
