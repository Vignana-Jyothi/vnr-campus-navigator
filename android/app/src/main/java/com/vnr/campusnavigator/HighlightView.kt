package com.vnr.campusnavigator

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.drawable.Drawable
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.ImageView

class HighlightView(context: Context, attrs: AttributeSet) : View(context, attrs) {

    private var rawImageHeight = 850
    private val paint = Paint().apply {
        color = Color.RED
        style = Paint.Style.STROKE
        strokeWidth = 5f
    }
    private var touchX = 0f
    private var touchY = 0f
    private var selectedRoom: String? = null

    private val roomCoordinates = mapOf(
        "202" to floatArrayOf(10f, 50f, 90f, 110f),
        "204" to floatArrayOf(10f, 110f, 90f, 170f),
        "206" to floatArrayOf(10f, 170f, 90f, 230f),
        "208" to floatArrayOf(15f, 230f, 100f, 290f),
        "210" to floatArrayOf(15f, 290f, 100f, 345f),
        "212" to floatArrayOf(15f, 345f, 100f, 430f),
        "214" to floatArrayOf(15f, 430f, 100f, 515f),
        "216" to floatArrayOf(15f, 515f, 100f, 600f),
        "218" to floatArrayOf(10f, 600f, 65f, 705f),
        "203" to floatArrayOf(120f, 50f, 210f, 110f),
        "205" to floatArrayOf(120f, 110f, 210f, 170f),
        "207" to floatArrayOf(120f, 170f, 210f, 230f),
        "209" to floatArrayOf(120f, 230f, 210f, 290f)
    )

    fun setSelectedRoom(room: String) {
        selectedRoom = room
        invalidate()
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        Log.d("HighlightView", "onDraw called")

        // Find the ImageView by ID
        val imageView = (parent as View).findViewById<ImageView>(R.id.floor_map)
        val drawable: Drawable = imageView.drawable
        if (drawable == null) {
            Log.e("HighlightView", "Drawable is null")
            return
        }

        val imageWidth = drawable.intrinsicWidth
        val imageHeight = drawable.intrinsicHeight

        val scaleX = imageView.width.toFloat() / imageWidth
        val scaleY = imageView.height.toFloat() / imageHeight

        val scaleFactor = Math.min(scaleX, scaleY)
        val imageScaleFactor = imageHeight.toFloat() / rawImageHeight.toFloat()

        val scaledWidth = imageWidth * scaleFactor
        val scaledHeight = imageHeight * scaleFactor

        val leftOffset = (imageView.width - scaledWidth) / 2
        val topOffset = (imageView.height - scaledHeight) / 2

        Log.d("HighlightView", "ImageView width: ${imageView.width}, height: ${imageView.height}")
        Log.d("HighlightView", "Drawable width: $imageWidth, height: $imageHeight")
        Log.d("HighlightView", "Scale factor: $scaleFactor")
        Log.d("HighlightView", "ImageScale factor: $imageScaleFactor")
        Log.d("HighlightView", "Offsets - Left: $leftOffset, Top: $topOffset")
        Log.d("HighlightView", "Touch coordinates: $touchX, $touchY")

        selectedRoom?.let { roomKey ->
            val room = roomCoordinates[roomKey]
            if (room != null) {
                val adjustedX1 = room[0] * scaleFactor * imageScaleFactor + leftOffset
                val adjustedY1 = room[1] * scaleFactor * imageScaleFactor + topOffset
                val adjustedX2 = room[2] * scaleFactor * imageScaleFactor + leftOffset
                val adjustedY2 = room[3] * scaleFactor * imageScaleFactor + topOffset
                Log.d("HighlightView", "Drawing rect at: $adjustedX1, $adjustedY1, $adjustedX2, $adjustedY2")
                canvas.drawRect(adjustedX1, adjustedY1, adjustedX2, adjustedY2, paint)
            }
        }

        // Draw rectangle based on touch coordinates
        for (room in roomCoordinates.values) {
            val adjustedX1 = room[0] * scaleFactor * imageScaleFactor + leftOffset
            val adjustedY1 = room[1] * scaleFactor * imageScaleFactor + topOffset
            val adjustedX2 = room[2] * scaleFactor * imageScaleFactor + leftOffset
            val adjustedY2 = room[3] * scaleFactor * imageScaleFactor + topOffset

            if (touchX >= adjustedX1 && touchX <= adjustedX2 && touchY >= adjustedY1 && touchY <= adjustedY2) {
                Log.d("HighlightView", "Drawing rect at: $adjustedX1, $adjustedY1, $adjustedX2, $adjustedY2")
                canvas.drawRect(adjustedX1, adjustedY1, adjustedX2, adjustedY2, paint)
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
