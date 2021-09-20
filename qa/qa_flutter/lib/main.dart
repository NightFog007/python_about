import 'package:data_tables/data_tables.dart';
import 'package:flutter/material.dart';
import 'package:dio/dio.dart';
import 'data/dessert.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {


  var color_list = [Colors.black,Colors.black,Colors.black,Colors.black,Colors.black,Colors.black,Colors.black,Colors.black,Colors.black];

  final List<Dessert> _desserts = <Dessert>[];


  List<Dessert> _items = [];
  int _rowsOffset = 0;

  List res = [
    [
    ]
  ];

  // void gengxin() async {
  //   await getHttp();


  //   if (res.length > 0) {

  //     print('res有数据');
  //     print(res);

  //     for (var i in res) {
  //     var oneone = new Dessert(
  //         i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]);
  //     _desserts.add(oneone);
  //   }

  //   }
    



  Future getHttp() async {
    try {
      // Response response = await Dio().get("http://127.0.0.1:8011/case_data");

      // res = response.data;

      res=[1,2,3,4,5];
print(res);

      if (res.length > 0) {

      print('res有数据');
      print(res);

    //   for (var i in res) {
    //   var oneone = new Dessert(
    //       // i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10]);
    //       30,'网银跨行系统', 'tester', 108, 11, 13,12, '2020-12-02 22:19:22', '吴维明', 'ECIF','5-开发五中心');
    //       _desserts.add(oneone);
    // }


var names = ['缺陷密度','遗留缺陷比例','线上问题比例','严重问题比例','安全基线测试','代码评审','代码质量检查接入率','代码质量检查达标率','项目单元测试覆盖率']  ;  
var defines = ['本月发现缺陷总数/代码行数(千行)','遗留缺陷总数/发现缺陷总数*100%','线上问题总数/发现缺陷总数*100%','(严重问题总数+致命问题总数)/发现缺陷总数*100%','基础安全测试13项,不通过个数','每月>2次,代码量>20%','接入sonarqube服务数/项目服务总数','达标率=扫描指标合格服务数/项目服务总数','单元测试覆盖率'];

var real_res = ['12','16','5','12','0','99','100','100','33'];
var result=[1,1,1,1,1,1,1,1,1];


var cankao_res_for_math=[5,15,20,10,1,80,100,100,20];

var cankao_res=['密度<5','比例<15%','比例<20%','比例<10%','不符合项<1','得分>80分','100%','100%','>=20%'];


for(var i = 0; i<5;i++){
  var xx =int.parse(real_res[i]);
  if (xx<cankao_res_for_math[i]){
    result[i]=0;
  } else{
    result[i]=1;
  }
}
var xx =int.parse(real_res[5]);
if (xx>80){
  result[5]=0;
}

for(var i = 6; i<7;i++){
  var xx =int.parse(real_res[i]);
  if (xx==100){
    result[i]=0;
  } else{
    result[i]=1;
  }
}
xx =int.parse(real_res[8]);
if (xx>20){
  result[8]=0;
}
var result_chinese=['否','否','否','否','否','否','否','否','否'];
for(var i = 0 ; i <9;i++){
  if (result[i]==0){
  result_chinese[i]='是';
  }else{
    color_list[i]=Colors.red;
  }
}


// 1. 缺陷密度 : 本月发现缺陷总数/代码行数(千行)
// 2. 遗留缺陷比例: 遗留缺陷总数/发现缺陷总数*100%
// 3. 线上问题比例: 线上问题总数/发现缺陷总数*100%
// 4. 严重问题比例: (严重问题总数+致命问题总数)/发现缺陷总数*100%
// 5. 安全基线测试: 基础安全测试13项,不通过个数
// 6. 代码评审: 每月>2次,代码量>20%
// 7. 代码质量检查接入率及达标率: 接入率=接入sonarqube服务数/项目服务总数
//                         达标率=扫描指标合格服务数/项目服务总数
// 8. 项目单元测试覆盖率: devops扫描得到数据



    
     for( var n = 0; n<names.length; n++ ) { 
       
      var oneone = new Dessert( n+1,names[n],defines[n],real_res[n],cankao_res[n], result_chinese[n], '2020-12-02 22:19:22', );
      _desserts.add(oneone);
   } 



   
    }
    return _desserts;
    





    } catch (e) {
      print("错误请求");
      print(e);
      return 0;
    }
  }

  int _rowsPerPage = PaginatedDataTable.defaultRowsPerPage;
  // int _rowsPerPage = 9;

  int _sortColumnIndex;
  bool _sortAscending = true;

    @override
  void initState() {

     getHttp().then((value) {
      // _counter = value;
      _items = value;
      setState(() {});
    });

    super.initState();
  }



  // }

  void _sort<T>(Comparable<T> getField(Dessert d), int columnIndex, bool ascending) {
    _items.sort((Dessert a, Dessert b) {
      if (!ascending) {
        final Dessert c = a;
        a = b;
        b = c;
      }
      final Comparable<T> aValue = getField(a);
      final Comparable<T> bValue = getField(b);
      return Comparable.compare(aValue, bValue);
    });
    setState(() {
      _sortColumnIndex = columnIndex;
      _sortAscending = ascending;
    });
  }



  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // theme: ThemeData.dark(),
      debugShowCheckedModeBanner: false, // 加入这行代码,即可关闭'DEBUG'字样

      home: Scaffold(
        appBar: AppBar(
          title: const Text('项目质量统计报表'),
        ),
        body: NativeDataTable.builder(
          
          rowsPerPage: _rowsPerPage,
          itemCount: _items?.length ?? 0,
          firstRowIndex: _rowsOffset,
          handleNext: () async {
            setState(() {
              _rowsOffset += _rowsPerPage;
            });

            await new Future.delayed(new Duration(seconds: 1));
            // setState(() {
        
         
            // });
          },
          // handlePrevious: () {
          //   setState(() {
          //     _rowsOffset -= _rowsPerPage;
          //   });
          // },
          itemBuilder: (int index) {
            final Dessert dessert = _items[index];
            return DataRow.byIndex(
                index: index,
                selected: dessert.selected,
                // color: MaterialStateProperty.all(Colors.green),
                // onSelectChanged: (bool value) {
                //   if (dessert.selected != value) {
                //     setState(() {
                //       dessert.selected = value;
                //     });
                //   }
                // },
                cells: <DataCell>[
                  DataCell(Text('${dessert.id}')),
                  DataCell(Text('${dessert.sys_name}',textAlign: TextAlign.left)),
                  DataCell(Text('${dessert.tester}')),
                  DataCell(Text('${dessert.all_case_num}')),
                  DataCell(Text('${dessert.right_case}')),
                  DataCell(Text('${dessert.wrong_case}', style: TextStyle(color: color_list[index]),)),
                  // DataCell(Text('${dessert.pass_num}')),
                  DataCell(Text('${dessert.last_time}')),
                  // DataCell(Text('${dessert.manager}')),
                  // DataCell(Text('${dessert.app_name}')),
                  // DataCell(Text('${dessert.center}')),
                ]);
          },
          header: const Text('统计结果'),
          sortColumnIndex: _sortColumnIndex,
          sortAscending: _sortAscending,
          // onRefresh: () async {
          //   await new Future.delayed(new Duration(seconds: 3));

          //   setState(() {});
          //   return null;
          // },
          // onRowsPerPageChanged: (int value) {
          //   setState(() {
          //     _rowsPerPage = value;
          //   });
          //   print("New Rows: $value");
          // },
          // mobileItemBuilder: (BuildContext context, int index) {
          //   final i = _desserts[index];
          //   return ListTile(
          //     title: Text(i?.name),
          //   );
          // },
          // onSelectAll: (bool value) {
          //   for (var row in _items) {
          //     setState(() {
          //       row.selected = value;
          //     });
          //   }
          // },
          rowCountApproximate: true,
          // actions: <Widget>[
          //   IconButton(
          //     icon: Icon(Icons.info_outline),
          //     onPressed: () {
          //       // getHttp();
          //     },
          //   ),
          // ],
          // selectedActions: <Widget>[
          //   IconButton(
          //     icon: Icon(Icons.delete),
          //     onPressed: () {
          //       setState(() {
          //         for (var item in _items
          //             ?.where((d) => d?.selected ?? false)
          //             ?.toSet()
          //             ?.toList()) {
          //           _items.remove(item);
          //         }
          //       });
          //     },
          //   ),
          // ],
          columns: <DataColumn>[
            DataColumn(
                label: const Text('序号'),
                onSort: (int columnIndex, bool ascending) =>
                    _sort<num>((Dessert d) => d.id, columnIndex, ascending)),
            DataColumn(
                label: const Text('指标名',textAlign: TextAlign.center),
                tooltip:
                    'The total amount of food energy in the given serving size.',
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.sys_name, columnIndex, ascending)),
            DataColumn(
                label: const Text('指标定义'),
                tooltip:
                    'The total amount of food energy in the given serving size.',
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.tester, columnIndex, ascending)),
            DataColumn(
                label: const Text('当前指标'),
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.all_case_num, columnIndex, ascending)),
            DataColumn(
                label: const Text('参考指标'),
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.right_case, columnIndex, ascending)),
            DataColumn(
                label: const Text('是否达标'),
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.wrong_case, columnIndex, ascending)),
            // DataColumn(
            //     label: const Text('通过率 (%)'),
            //     numeric: true,
            //     onSort: (int columnIndex, bool ascending) => _sort<num>(
            //         (Dessert d) => d.pass_num, columnIndex, ascending)),
            DataColumn(
                label: const Text('最后统计时间'),
                tooltip:
                    'The amount of calcium as a percentage of the recommended daily amount.',
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.last_time, columnIndex, ascending)),
            // DataColumn(
            //     label: const Text('项目经理'),
            //     numeric: true,
            //     onSort: (int columnIndex, bool ascending) => _sort<String>(
            //         (Dessert d) => d.manager, columnIndex, ascending)),
            // DataColumn(
            //     label: const Text('应用名称'),
            //     numeric: true,
            //     onSort: (int columnIndex, bool ascending) => _sort<String>(
            //         (Dessert d) => d.app_name, columnIndex, ascending)),
            // DataColumn(
            //     label: const Text('开发中心'),
            //     numeric: true,
            //     onSort: (int columnIndex, bool ascending) => _sort<String>(
            //         (Dessert d) => d.center, columnIndex, ascending)),
          ],
        ),
      ),
    );
  }


}


