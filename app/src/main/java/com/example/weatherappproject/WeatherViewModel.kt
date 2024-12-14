package com.example.weatherappproject

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import com.example.weatherappproject.RetrofitInstance
import com.example.weatherappproject.WeatherApi


class WeatherViewModel : ViewModel() {

    // LiveData to hold weather data
    private val _weatherData = MutableLiveData<WeatherResponse?>()
    val weatherData: LiveData<WeatherResponse?> get() = _weatherData

    // Function to set weather data
    fun setWeatherData(weatherResponse: WeatherResponse) {
        _weatherData.value = weatherResponse
    }

    // Function to fetch weather data from the API
    fun getWeather(cityName: String): Call<WeatherResponse> {
        val apiService = RetrofitInstance.api  // This should now work without errors
        return apiService.getWeather(cityName, "929c0ec6c5220a1b08e3746956fcc759") // Replace with your API key
    }

    // Fetch and set weather data
    fun fetchWeatherData(cityName: String) {
        getWeather(cityName).enqueue(object : Callback<WeatherResponse> {
            override fun onResponse(call: Call<WeatherResponse>, response: Response<WeatherResponse>) {
                if (response.isSuccessful) {
                    // On successful response, set the weather data
                    response.body()?.let { weatherData ->
                        setWeatherData(weatherData)
                    }
                } else {
                    // Handle error
                    _weatherData.value = null
                }
            }

            override fun onFailure(call: Call<WeatherResponse>, t: Throwable) {
                // Handle failure
                _weatherData.value = null
            }
        })
    }
}


