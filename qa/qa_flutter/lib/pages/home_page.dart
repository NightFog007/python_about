import 'package:flutter/material.dart';
import 'home/home_content.dart';

class HomePage extends StatefulWidget {

  HomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title),),
      body: HomeContent(count: _counter,),
      floatingActionButton: _buildHomeButton()
    );
  }

  //抽离成方法单独管理
  Widget _buildHomeButton() {
    return FloatingActionButton(
      onPressed: _incrementCounter,
      tooltip: 'Increment',
      child: Icon(Icons.add),
    );
  }
}