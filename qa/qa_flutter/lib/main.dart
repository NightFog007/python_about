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

    var color_list = [
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    //     Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
    // Colors.green,
  ];


  final List<Dessert> _desserts = <Dessert>[];
  final baseUrl = "http://127.0.0.1:8008";

  List<Dessert> _items = [];
  int _rowsOffset = 0;

  List res = [[]];


  var new_result;

  Future getHttp() async {
    try {
      Response response = await Dio().get(baseUrl + "/new_result");

      new_result = response.data;
      print(new_result);


      if (res.length > 0) {
        print('res有数据');
        print(res);

        var names = [
          '缺陷密度',
          '遗留缺陷比例',
          '线上问题比例',
          '严重问题比例',
          '安全基线测试',
          '代码评审',
          '代码质量检查接入率',
          '代码质量检查达标率',
          '项目单元测试覆盖率'
        ];
        var defines = [
          '本月发现缺陷总数/代码行数(千行)',
          '遗留缺陷总数/发现缺陷总数*100%',
          '线上问题总数/发现缺陷总数*100%',
          '(严重问题总数+致命问题总数)/发现缺陷总数*100%',
          '基础安全测试13项,不通过个数',
          '每月>2次,代码量>20%',
          '接入sonarqube服务数/项目服务总数',
          '达标率=扫描指标合格服务数/项目服务总数',
          '单元测试覆盖率'
        ];

        var cankao_res = [
          '密度<5',
          '比例<15%',
          '比例<20%',
          '比例<10%',
          '不符合项<1',
          '得分>80分',
          '100%',
          '100%',
          '>=20%'
        ];


     
        print(new_result.length);
        for (var n = 0; n < new_result.length; n++) {
          color_list.add(Colors.green);
          var oneone = new Dessert(
            n + 1,
            new_result[n][0],
            new_result[n][1],
            new_result[n][2],
            new_result[n][3],
            new_result[n][4],
            new_result[n][5],
            // new_result[n][6],
          );
          print(oneone);
          if (new_result[n][4] == "Failed") {
            color_list[n] = Colors.red;
          }

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

  void _sort<T>(
      Comparable<T> getField(Dessert d), int columnIndex, bool ascending) {
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
          },

          itemBuilder: (int index) {
            final Dessert dessert = _items[index];
            return DataRow.byIndex(
                index: index,
                selected: dessert.selected,
                cells: <DataCell>[
                  DataCell(Text('${dessert.id}')),
                  DataCell(
                      Text('${dessert.sys_name}', textAlign: TextAlign.left)),
                  DataCell(Text('${dessert.tester}')),
                  DataCell(Text(
                    '${dessert.all_case_num}',
                    style: TextStyle(fontWeight: FontWeight.w700),
                  )),
                  DataCell(Text('${dessert.right_case}')),
                  DataCell(Text(
                    '${dessert.wrong_case}',
                    style: TextStyle(color: color_list[index]),
                  )),
                  DataCell(Text('${dessert.last_time}')),
                ]);
          },
          header: const Text('统计结果'),
          sortColumnIndex: _sortColumnIndex,
          sortAscending: _sortAscending,

          rowCountApproximate: false, //最下方是否自动刷

          columns: <DataColumn>[
            DataColumn(
                label: const Text('序号'),
                onSort: (int columnIndex, bool ascending) =>
                    _sort<num>((Dessert d) => d.id, columnIndex, ascending)),
            DataColumn(
                label: const Text('指标名', textAlign: TextAlign.center),
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
            DataColumn(
                label: const Text('最后统计时间'),
                tooltip:
                    'The amount of calcium as a percentage of the recommended daily amount.',
                numeric: true,
                onSort: (int columnIndex, bool ascending) => _sort<String>(
                    (Dessert d) => d.last_time, columnIndex, ascending)),
          ],
        ),
      ),
    );
  }
}
