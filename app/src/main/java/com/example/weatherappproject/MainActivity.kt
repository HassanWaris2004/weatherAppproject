package com.example.weatherappproject

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.weatherappproject.databinding.ActivityMainBinding
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class MainActivity : AppCompatActivity() {

    // ViewBinding instance for the layout
    private lateinit var binding: ActivityMainBinding

    // ViewModel instance
    private lateinit var weatherViewModel: WeatherViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Inflate the layout using ViewBinding
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Initialize ViewModel using ViewModelProvider
        weatherViewModel = ViewModelProvider(this).get(WeatherViewModel::class.java)

        // Set a click listener on the button to get weather data
        binding.buttonGetWeather.setOnClickListener {
            val cityName = binding.editTextCity.text.toString()
            if (cityName.isNotEmpty()) {
                fetchWeather(cityName)
            } else {
                Toast.makeText(this, "Please enter a city name", Toast.LENGTH_SHORT).show()
            }
        }

        // Observing the LiveData from ViewModel (in case you need to update UI from ViewModel)
        weatherViewModel.weatherData.observe(this, Observer { weatherResponse ->
            // This will be triggered when the weather data is fetched successfully
            weatherResponse?.let {
                binding.textViewCity.text = it.name
                binding.textViewTemperature.text = "${it.main.temp} °C"
                binding.textViewDescription.text = it.weather[0].description
            }
        })
    }

    // Function to fetch weather data from the API using Retrofit
    private fun fetchWeather(cityName: String) {
        // Call the ViewModel function to fetch weather data
        weatherViewModel.getWeather(cityName).enqueue(object : Callback<WeatherResponse> {
            override fun onResponse(call: Call<WeatherResponse>, response: Response<WeatherResponse>) {
                if (response.isSuccessful) {
                    // On success, the response body is passed into the observer
                    response.body()?.let { weatherData ->
                        // Update the ViewModel with fetched data
                        weatherViewModel.setWeatherData(weatherData)
                    }
                } else {
                    // Show error if response is not successful
                    Toast.makeText(this@MainActivity, "Error fetching data", Toast.LENGTH_SHORT).show()
                }
            }

            override fun onFailure(call: Call<WeatherResponse>, t: Throwable) {
                // Handle network failure
                Toast.makeText(this@MainActivity, "Network error", Toast.LENGTH_SHORT).show()
            }
        })
    }
}









