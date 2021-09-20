
import 'package:dio/dio.dart';

class MyClass {
  
  void getHttp(input_text, input_type , textKey) async {
    try {
      Response response = await Dio().get(
          "http://japi.juhe.cn/charconvert/change.from?text=" +
              input_text +
              "&type=" +
              input_type +
              "&key=3f598eb8834c968feefe1a63f1fbeabe");

      var tmp = response.data;
      print("-------------");

      var new_index = tmp.indexOf('"outstr":"') + 10;

      var final_text = tmp.substring(new_index);

      var xx = final_text.indexOf('"');
      var yyy = final_text.substring(0, xx);

      textKey.currentState.onPressed(yyy);
    } catch (e) {
      print(e);
    }
  }


}