import 'package:flutter/material.dart';
// 抽离成组件单独管理
class HomeContent extends StatelessWidget {
  final int count;

  HomeContent({this.count});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text('You have pushed the button this many times:',),
          Text('$count',
            style: Theme.of(context).textTheme.display1,
          ),
        ],
      ),
    );
  }
}
