import 'package:flutter/material.dart';
import 'models.dart';

class WorkDetail extends StatelessWidget {
  final Work work;

  WorkDetail({this.work});

  bodyWidget(BuildContext context) => Stack(
        children: <Widget>[
          Positioned(
              height: MediaQuery.of(context).size.height / 1.5,
              width: MediaQuery.of(context).size.width - 25,
              left: 10.0,
              top: MediaQuery.of(context).size.height * 0.13,
              child: Card(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0),
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: <Widget>[
                    SizedBox(
                      height: 100.0,
                    ),
                    //Text(
                    //pokemon.name,
                    // style:
                    //   TextStyle(fontSize: 25.0, fontWeight: FontWeight.bold),
                    // ),
                    Text("${work.farmer_name}"),
                    Text("${work.lat}"),
                    Text("${work.lng}"),
                    Text("${work.dateStart}"),
                    Text("${work.dateEnd}"),
                    Text("${work.area}"),
                    Text("${work.rice_type}"),
                    Text("${work.repairTime}"),
                    Text("${work.harverstime}"),
                    Text("${work.money}"),
                    Text("${work.moneyStatus}"),
                    Text("${work.workStatus}"),
                    Text("${work.tractor}"),
                    Text("${work.tractorStatus}"),
                    // Text("${work.money}"),
                    //Text("จำนวนสินค้าที่มี"+ "${pokemon.nextEvolution}"),
                    // Text("${farmer.store}"),
                    // Text("จำนวนสินค้าที่ต้องการซื้อ", style: TextStyle(fontWeight: FontWeight.bold)),
                    // TextField(
                    //     decoration: InputDecoration(
                    //       border: OutlineInputBorder()
                    //     )
                    //   ),
/*
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: farmer.weaknesses
                            .map((n) => FilterChip(
                                  backgroundColor: Colors.red,
                                  label: Text(
                                    "สั่งซื้อสินค้า",
                                    style: TextStyle(color: Colors.white),
                                  ),
                                  
                                  onSelected: (b) {},
                                ))
                                
                            .toList(),
                  )
                  */
                  ],
                ),
                //   ),
                // ),

                // Align(
                //   alignment: Alignment.topCenter,
                //   child: Hero(
                //       tag: farmer.name,
                //       child: Container(
                //         height: 190.0,
                //         width: 190.0,
                //         decoration: BoxDecoration(
                //             image: DecorationImage(
                //                 fit: BoxFit.cover,
                //                 image: FARMER_IMAGES.containsKey(farmer.cid) ?
                //                   NetworkImage(farmer_IMAGES[farmer.cid]):
                //                   NetworkImage('http://picsum.photos/200'))),
                //       )),
                // )
              ))
        ],
      );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.purple[50],
      appBar: AppBar(
        elevation: 0.0,
        backgroundColor: Colors.green,
        // title: Text(work.workId),
      ),
      body: bodyWidget(context),
    );
  }
}
