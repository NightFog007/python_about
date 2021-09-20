import 'new_text.dart';

import 'package:flutter/material.dart';

import 'package:shared_preferences/shared_preferences.dart';

import 'dart:async';
import 'package:flutter/services.dart';

class ToastHelper {
  static void showToast(BuildContext context, String text) {
    const style = TextStyle(color: Colors.white, fontSize: 14.0);

    Widget widget = Center(
      child: Material(
        child: Container(
          color: Colors.black.withOpacity(0.5),
          padding: const EdgeInsets.symmetric(vertical: 5.0, horizontal: 10.0),
          child: Text(
            text,
            style: style,
          ),
        ),
      ),
    );
    var entry = OverlayEntry(
      builder: (_) => widget,
    );

    Overlay.of(context).insert(entry);

    Timer(const Duration(seconds: 2), () {
      entry?.remove();
    });
  }
}

class ClipboardData {
  /// Creates data for the system clipboard.
  const ClipboardData({this.text});

  /// Plain text variant of this clipboard data.
  final String text;
}

class Clipboard {
  Clipboard._();

  static const String kTextPlain = 'text/plain';

  /// Stores the given clipboard data on the clipboard.
  ///将ClipboardData中的内容复制的粘贴板
  static Future<void> setData(ClipboardData data) async {
    await SystemChannels.platform.invokeMethod<void>(
      'Clipboard.setData',
      <String, dynamic>{
        'text': data.text,
      },
    );
  }
}

typedef OnPressed();

class CopyButtonWidget extends StatefulWidget {
  OnPressed onPressed;

  CopyButtonWidget({this.onPressed});

  @override
  State<StatefulWidget> createState() {
    return _CopyButtonWidgetState(onPressed);
  }
}

class _CopyButtonWidgetState extends State<CopyButtonWidget> {
  OnPressed _onPressed;

  Future<SharedPreferences> _prefs = SharedPreferences.getInstance();

  _CopyButtonWidgetState(this._onPressed);

  GlobalKey<TextWidgetState> key = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return Center(
      child:
          //   FlatButton(
          //   onPressed: _onPressed,
          //   padding: EdgeInsets.all(8),
          //   splashColor: Colors.green,
          //   child: Text("提交"),
          //   textColor: Color(0xffFfffff),
          //   color: Colors.blue,
          //   highlightColor: Color(0xffF88B0A),
          // ),
          RaisedButton(
        padding: EdgeInsets.all(8),
        splashColor: Colors.green,
        textColor: Color(0xffFfffff),
        color: Colors.blue,
        highlightColor: Color(0xffF88B0A),
        child: const Text('一键复制'),
        onPressed: () async {
          final SharedPreferences prefs = await _prefs;
          var tt_text = prefs.getString("res_text");
          ClipboardData data = new ClipboardData(text: tt_text);
          Clipboard.setData(data);
          ToastHelper.showToast(context, "复制成功");
        },
      ),
    );
  }
}
