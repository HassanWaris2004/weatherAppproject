package com.example.weatherappproject

// WeatherResponse class containing the data structure for the API response
data class WeatherResponse(
    val name: String, // City name
    val main: Main, // Main weather data (temperature, etc.)
    val weather: List<Weather> // Weather conditions (description, etc.)
)

// Main data class for temperature information
data class Main(
    val temp: Double // Temperature in Celsius
)

// Weather data class for weather conditions like description
data class Weather(
    val description: String // Weather description (e.g., "clear sky")
)
