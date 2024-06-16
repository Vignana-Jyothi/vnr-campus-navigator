package com.vnr.campusnavigator

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Spinner
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var highlightView: HighlightView
    private lateinit var roomSelector: Spinner
    private var selectedRoom: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        highlightView = findViewById(R.id.highlight_view)
        roomSelector = findViewById(R.id.room_selector)

        // Room numbers
        val roomNumbers = arrayOf("202", "204", "206", "208", "210", "212", "214", "216", "218", "203", "205", "207", "209")

        // Set up the Spinner with room numbers
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_item, roomNumbers)
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        roomSelector.adapter = adapter

        // Handle Spinner selection
        roomSelector.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>, view: View?, position: Int, id: Long) {
                selectedRoom = roomNumbers[position]
                highlightView.setSelectedRoom(selectedRoom!!)
            }

            override fun onNothingSelected(parent: AdapterView<*>) {
                // Do nothing
            }
        }

        // Restore the selected room if available
        savedInstanceState?.let {
            selectedRoom = it.getString("selectedRoom")
            selectedRoom?.let { room ->
                roomSelector.setSelection(roomNumbers.indexOf(room))
                highlightView.setSelectedRoom(room)
            }
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putString("selectedRoom", selectedRoom)
    }
}
