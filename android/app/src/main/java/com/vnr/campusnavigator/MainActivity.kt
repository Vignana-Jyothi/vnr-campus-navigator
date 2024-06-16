package com.vnr.campusnavigator

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("HighlightView", "from the main activity")
        setContentView(R.layout.activity_main)
    }
}
