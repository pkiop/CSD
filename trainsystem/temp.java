package com.example.pkiop.myevent;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.GestureDetector;
import android.view.KeyEvent;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    TextView textView;
    GestureDetector detector; //움직이는 속도같은 걸 측정하고 싶을 때
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = (TextView) findViewById(R.id.textView);

        View view = findViewById(R.id.view1);
        //on TouchListener => 좀더 상세한 터치 조작 가능
        view.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                int action = event.getAction();

                float curX = event.getX();
                float curY = event.getY();

                if(action == MotionEvent.ACTION_DOWN){
                    println("손가락 눌렸음 : " + curX + ", " + curY);
                }
                else if(action == MotionEvent.ACTION_MOVE){
                    println("손가락 움직임 : " + curX + ", " + curY);
                }
                else if(action == MotionEvent.ACTION_UP){
                    println("손가락 땠다. : " + curX + ", " + curY);
                }
                return true;
            }//움직이는 순간 계속 터치된다.
        });

        detector = new GestureDetector(this, new GestureDetector.OnGestureListener() {
            @Override
            public boolean onDown(MotionEvent e) {
                println("onDown() 눌러짐");
                return true;
            }

            @Override
            public void onShowPress(MotionEvent e) {
                println("onShowPress() 눌러짐");

            }

            @Override
            public boolean onSingleTapUp(MotionEvent e) {
                println("onSingleTapUp() 눌러짐");
                return true;
            }

            @Override
            public boolean onScroll(MotionEvent e1, MotionEvent e2, float distanceX, float distanceY) {
                println("onScroll() 눌러짐");
                return true;
            }

            @Override
            public void onLongPress(MotionEvent e) {
                println("onLongPress() 눌러짐");

            }

            @Override
            public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
                println("onFling() 눌러짐");
                return true;
            }
        });
        View view2 = findViewById(R.id.view2);
        view2.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
               detector.onTouchEvent(event);
               return true;
            }
        });
    }


    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
       if(keyCode == KeyEvent.KEYCODE_BACK){ // 원래 앱 백키를 누르면 바로 종료되는데 이렇게 한번 입력 받고 다시 눌렀을 때 종료할 수 있게 할 수 있다.
           Toast.makeText(this, "시스템 BACK 버튼 눌림.", Toast.LENGTH_LONG).show();
           return true;
       }
       return false;
    }

    public void println(String data){
        textView.append(data+"\n");
    }
}