package com.vnr.campusnavigator

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.view.View

class HighlightView(context: Context, attrs: AttributeSet) : View(context, attrs) {

    private val paint = Paint().apply {
        color = Color.YELLOW
        style = Paint.Style.STROKE
        strokeWidth = 5f
    }
    private var touchX = 0f
    private var touchY = 0f

    private val roomCoordinates = arrayOf(
        floatArrayOf(10f, 50f, 90f, 110f),  // Room 202
        floatArrayOf(10f, 110f, 90f, 170f), // Room 204
        floatArrayOf(10f, 170f, 90f, 230f), // Room 206
        floatArrayOf(15f, 230f, 100f, 290f), // Room 208
        floatArrayOf(15f, 290f, 100f, 345f), // Room 210
        floatArrayOf(15f, 345f, 100f, 430f), // Room 212
        floatArrayOf(15f, 430f, 100f, 515f), // Room 214
        floatArrayOf(15f, 515f, 100f, 600f), // Room 216
        floatArrayOf(10f, 600f, 65f, 705f),  // Room 218
        floatArrayOf(120f, 50f, 210f, 110f), // Room 203
        floatArrayOf(120f, 110f, 210f, 170f), // Room 205
        floatArrayOf(120f, 170f, 210f, 230f), // Room 207
        floatArrayOf(120f, 230f, 210f, 290f)  // Room 209
        // Add more room coordinates as needed
    )

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        Log.d("HighlightView", "onDraw called")
        for (room in roomCoordinates) {
            if (touchX >= room[0] && touchX <= room[2] && touchY >= room[1] && touchY <= room[3]) {
                Log.d("HighlightView", "Drawing rect at: $touchX, $touchY")
                canvas.drawRect(room[0], room[1], room[2], room[3], paint)
            }
        }
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        Log.d("HighlightView", "onTouchEvent called: ${event.action}")
        if (event.action == MotionEvent.ACTION_MOVE || event.action == MotionEvent.ACTION_DOWN) {
            touchX = event.x
            touchY = event.y
            invalidate()
            return true
        }
        return false
    }
}
