import 'new_text.dart';

import 'package:flutter/material.dart';

//调用方法
// ButtonWidget(
//       onPressed: () {
//             getHttp(input_text, "1");
//       },
// ),

typedef OnPressed();

class ButtonWidget extends StatefulWidget {
  OnPressed onPressed;

  ButtonWidget({this.onPressed});

  @override
  State<StatefulWidget> createState() {
    return _ButtonWidgetState(onPressed);
  }
}

class _ButtonWidgetState extends State<ButtonWidget> {
  OnPressed _onPressed;

  _ButtonWidgetState(this._onPressed);

  GlobalKey<TextWidgetState> key = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return Center(

      child: FlatButton(
      onPressed: _onPressed,
      padding: EdgeInsets.all(8),
      splashColor: Colors.green,
      child: Text("提交"),
      textColor: Color(0xffFfffff),
      color: Colors.blue,
      highlightColor: Color(0xffF88B0A),
    ),
    );
  }
}