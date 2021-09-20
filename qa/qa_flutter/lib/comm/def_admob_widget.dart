import 'package:admob_flutter/admob_flutter.dart';
import 'package:flutter/material.dart';
import './admob_info.dart';


void handleEvent(AdmobAdEvent event, Map<String, dynamic> args, String adType) {
  switch (event) {
    case AdmobAdEvent.loaded:
      print('New Admob $adType Ad loaded!');
      break;
    case AdmobAdEvent.opened:
      print('Admob $adType Ad opened!');
      break;
    case AdmobAdEvent.closed:
      print('Admob $adType Ad closed!');
      break;
    case AdmobAdEvent.failedToLoad:
      print('Admob $adType failed to load. :(');
      break;
    default:
  }
}

//返回横幅广告控件
//! 使用方式 - ad_banner()当做控件用.
Widget ad_banner() {
  return AdmobBanner(
    adUnitId: test_banner,
    // adSize: bannerSize,
    adSize: AdmobBannerSize(width: 320, height: 50, name: 'BANNER'),
    listener: (AdmobAdEvent event, Map<String, dynamic> args) {
      handleEvent(event, args, 'Banner');
    },
  );
}

//返回点击弹出广告方法
//! 使用方式 - 提供方法给按钮点击使用: onPressed: ad_button,
void ad_button() async {
  AdmobInterstitial interstitialAd;

  interstitialAd = AdmobInterstitial(
    adUnitId: test_intersitital,
    listener: (AdmobAdEvent event, Map<String, dynamic> args) {
      if (event == AdmobAdEvent.closed) interstitialAd.load();
      handleEvent(event, args, 'Interstitial');
    },
  );
  interstitialAd.load();

  if (await interstitialAd.isLoaded) {
    interstitialAd.show();
  } else {
    print("Interstitial ad is still loading...");
  }
}

