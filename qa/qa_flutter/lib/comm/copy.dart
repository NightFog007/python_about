import 'package:flutter/material.dart';
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
  const ClipboardData({ this.text });

  /// Plain text variant of this clipboard data.
  final String text;
}


class Clipboard {
  Clipboard._();

  // Constants for common [getData] [format] types.

  /// Plain text data format string.
  ///
  /// Used with [getData].
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
