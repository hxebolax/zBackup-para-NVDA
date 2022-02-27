# Kullanım kılavuzu:

zYedekleme, işletim sistemini içeren bölümün yedek kopyalarını oluşturmamıza olanak tanır.  

Bu, Windows kurulumunu içeren diskin veya bölümün geri yüklenebilmesi için kaydedilebileceği anlamına gelir.  

zYedekleme, çalışan uygulamaları kapatmaya veya yaptığımız işlemleri durdurmaya gerek kalmadan etkin yedeklemeler yapabilir.  

[Bu eklenti, Drive Snapshot uygulamasını temel alır.](http://www.drivesnapshot.de/en/index.htm)  

zYedekleme, WinPE gibi yardıma veya harici araçlara ihtiyaç duymadan bir yedekleme yapıp geri yükleyebilmemiz için yaygın ve gerekli eylemleri basitleştirir.  

Yedek kopyalar oluşturmanın yanı sıra bu kopyaları geri yükleyebilecek, sanal birimler olarak bağlayabilecek ve tüm bunları erişilebilir bir şekilde gerçekleştirebileceğiz.  

zYedekleme, Drive Snapshot'ı temel alır, bu nedenle NVDA'nın dışında bir uygulama kullanır. Söz konusu uygulama 500 KB'den daha azdır ve eklentiyi ilk başlattığımızda resmi sayfadan indirilecektir.  

zYedekleme eklentisi her güncellendiğinde, Uygulama da resmi sayfasından en güncel sürüme yükseltilir.  

Drive SnapShot ücretsiz bir uygulama değildir ve sınırlamaları vardır. Uygulamanın tamamı 30 gün boyunca kullanılabilir, ancak bu süreden sonra Yedekleme, yedeklemeyi geri yükleme ve Yedeği sanal sürücü olarak bağlama özellikleri kullanılabilecektir.  

Uygulama sayfasında, kişisel kullanım için yeterli olan en temel lisansıyla Drive SnapShot'ı 39 Euro'ya satın alabiliriz.  

Lisans satın alınırsa, zYedekleme eklentisini her güncellediğimizde, uygulamanın güncellenmiş bir sürümünü indirirken, yeniden lisanslamamız gerekeceğinden, satın aldığımız lisansı güvenilir bir yerde saklamamız gerekir.  

## *** çok önemli bilgiler ***

zYedekleme, mükemmel sonuçlarla farklı ortamlarda ve durumlarda test edilmiştir.  
Ancak bilgisayar dünyasında daima olumsuzluklar  ve arızalar olabilir, bu nedenle yalnızca kötü bir sistem geri yüklemesinden kurtulmak için yeterli bilgiye sahip kişiler için önerilen bir eklentidir...  
Bu, bilgileri kurtarmak, işletim sistemini kurmak ve nihayetinde, bir şeyler ters giderse Windows'a yeniden sahip olabilmek için başka bir ortamdan nasıl önyükleme yapılacağını bilmek gerektiği anlamına gelir.  

Eklentiyi kullanırken, Yedekleme, geri yükleme, diğer kullanımlar esnasında ortaya çıkabilecek sorunlar ve veri kaybından eklenti geliştiricisi sorumlu değildir.  

## *** Sorunsuz kullanım için uyarı ***

zYedek, aynı Windows bölümünden geri yükleme, yedekleme adlarında istenmeyen semboller kullanma, alan eksikliğine karşı koruma vb. gibi hata yapmaktan kaçınmak için korumalar içerir. Ancak, birkaç hususun dikkate alınması gerekir.  

Yedeklemeler yalnızca Windows dışındaki bir bölümden veya diskten geri yüklenebilir. Kopyalar harici medyadan da geri yüklenebilir, ancak söz konusu medyanın okuma hızını hesaba katmamız gerekecek. Yavaş ortam, geri yükleme sırasında sorunlara neden olabilir, bu nedenle harici SSD sürücüleri veya yüksek hızlı USB Type-C depolama yöntemi kullanılması önerilir.  

Güvenli olmayan modda BIOS'un yedek bir kopyasını oluşturursak, o moddayken söz konusu kopyayı geri yükleyebileceğimizi unutmamalıyız. Güvenli moda geçersek, güvenli olmayan modda yapılan kopya artık geri yüklenemez. Her kopya, ilgili donanım ve ilgili donanım yapılandırmasıyla geri yüklenmelidir.  

Benzer şekilde, BitLocker korumalı sürücüleri yedeklemek için zYedekleme kullanmamanız önerilir.  

zYedekleme, Windows 10 ve 11'de test edilmiştir, ancak uygulamanın belgelerine göre Windows 7 ve 8'de de geçerlidir.  

Yedekleri kaydettiğimiz dizin yolunun boşluk içermemesi önerilir.  

zYedekleme, NVDA'nın taşınabilir sürümlerinde kullanılamaz.  

## zYedekleme Arayüzü:  

zYedekleme, az seçeneğe sahip olmayı ve net olmayı amaçlar, bu nedenle her zaman ne yapacağı konusunda ve izlenecek adımlar hakkında bize bilgi mesajları verecektir.  

Ana ekrandan yedekleme yapabiliriz.  

Ana pencereyi başlatmak için NVDA / Tercihler / Girdi hareketleri / zBackup kategorisinden bir hareket eklemeniz gerekir.  

Atadığımız kısa yol ile ana pencereyi açtıktan sonra, yedeği kaydedeceğimiz dizini içeren salt okunur bir kutuya erişiriz. Bir defa tab tuşuna basarsak söz konusu dizini seçmemize izin verecek Dizin seç düğmesinin üzerine odaklanırız.  

Yedeklemeler bu dizindeki alt klasörlere kaydedilecektir. Bu klasörde boşluk olmaması önerilir.  

Tekrar sekme tuşuna bastığımızda, Yedekleme dosyasının Adını girin adlı bir düzenleme kutusuna düşeriz. Bu kutuya yedeğimizin tanımlayıcı adını koyacağız.  

Klasörlerde ve dosyalarda bu kutuda Windows tarafından izin verilmeyen boşluklara ve karakterlere izin verilmez. Bu karakterler, üçlü tırnak işaretleri arasında yer alan aşağıdaki gibidir:  

"""\ / : * ? » < > |"""  

Bu tanımlama adı, alt klasörü ve yedeğin farklı dosyalarını adlandırmaya hizmet edecektir.  

Tekrar tab tuşuna basarsak her bir yedekleme dosyasının boyutunu seçebileceğimiz bir birleşik giriş kutusuna erişeceğiz. 500 mb ile 10 GB arasında seçim yapabiliriz.  

Bu, yedekleme yaptığınızda ortaya çıkan dosyaların o boyutta olacağı anlamına gelir. Örnek vermek gerekirse: Windows bölümümüz yaklaşık 60 GB boyutundaysa, ortaya çıkan kopyanın toplam boyutu yaklaşık 20 ila 30 GB olacaktır. Ortaya çıkan dosyaları 10 GB olarak seçersek yaklaşık 3 dosya oluşturacaktır.  

Tekrar sekme tuşuna basarsak, Yedeklemeyi başlat düğmesine erişeceğiz. Tüm veriler doğru bir şekilde doldurulursa ve alan ve konum koşulları sağlanırsa, bize her zaman ne yapacağını gösteren yedeklemeyi başlatma imkanı verecektir.  

Tekrar sekme tuşuna basarsak Menu butonunun üzerine odaklanırız. Üzerine bastığımızda aşağıdaki seçeneklerle bağlamsal bir menü görüntülenecektir:  

* Yedeklemeyi geri yükle: Bu seçenek ile bir yedeği geri yükleyebiliriz. Mesajlarla yönlendirileceğiz. Geri yüklenecek görüntüyü seçme ve kabul etme noktasına ulaştığınızda, işlemin artık geri alınamayacağını ve sistemin geri yükleneceğini akılda tutmak önemlidir.
* Bir yedekten sanal diski bağlayın: Bu seçenekle, bilgisayarımızın boş bir birimini seçme ve sanal olarak bir kopyasını bağlama olanağına sahip olacağız. Bu, bir yedeklemeden kurtarmak istediğimiz belirli bir şey varsa ve onu tamamen geri yüklemek istemiyorsak iyidir.
* Sanal sürücülerin bağlantısını kes: Bu seçenek, zYedekleme ile bağladığımız tüm sanal sürücülerin bağlantısını kesecektir. Tek tek seçmek mümkün değil. Bu seçenek, herhangi bir bağlantımız olmasa bile başarıyla yürütülecektir.
* Drive Snapshot uygulamasını çalıştır: Bu seçenek ile Uygulamayı başlatacağız ve grafik arayüz modunda kullanabileceğiz. Lisans almışsak seri numarasını da kaydedebiliyoruz.

Tüm kontroller, arayüzde ilerlerken duyurulan klavye kısayollarına sahiptir.  

## Diğer bilgiler:  

Yedeklerken, hedef diskin veya bölümün sistem bölümünün boyutunda olması gerekir. Sistem bölümü 60 GB'a sahipse, kopya daha sonra yarısını veya daha azını kaplasa bile hedef bölümde 60 GB boş alan olması gerekir. Bu güvenlik içindir.  

Bir şeyler ters giderse diye önyüklenebilir bir medyaya sahip olmak iyi bir fikirdir. Bu tür ortamlarda bir WinPE ve Sürücü Anlık Görüntüsü önerilir. Bu şekilde, sistemi yedekten kurtarabiliriz.  

zYedekleme, Windows üzerinde herhangi bir değişiklik yapılmadan test edilmiştir. İnternette dolaşan bazı değiştirilmiş Windows sürümlerinde düzgün çalışması garanti edilmez.  

Hatalı bir geri yükleme sonucunda neler yapabileceğiniz konusunda bilgiye sahip değilseniz, zYedekleme eklentisini kullanmamanızı tavsiye ediyoruz.  

## Bilinen Sorunlar:

Eklenti, farklı donanım ve konfigürasyona sahip birkaç bilgisayarda ve sanal makinelerde test edilmiştir.  

Geri yüklemeye başladığında, bilgisayarın fanlarının çalışmaya başladığını ve onarım bittiğinde durduğunu duyabiliriz. Aynı şekilde, takılı kulaklıklarımız varsa, kulaklıklardaki tıklamalarla yeniden başlatmaları algılayabiliriz.  

Güvenli modda, bazen yedekleme geri yüklendikten sonra sistem açılmaz ve üreticinin logosunda kalır.  

Bu gibi durumlarda, birkaç dakika beklemeniz ve bilgisayarı kapatmanız önerilir.  

Bir sonraki başlatışınızda, Windows bir disk kontrolü yapmak isteyip istemediğinizi, kontrolün kendisini başlatmak isteyip istemediğinizi soracak, erişilemeyen bir ekranla size başka bir kurtarma seçeneği denemenizi ve bilgisayarınızı kapatmanızı söyleyecektir.  

Enter'a basarsak, kapanacaktır. Bilgisayarı bir sonraki başlatışımızda, Windows önyüklemesi gerçekleşir.  

Bu, çok ince olan güvenli mod korumasıdır, ancak aslında geri yükleme başarılı olmuştur.  

Aynı şekilde, bazen Windows'ta başlar ve zaten oturum açtığımızda, hataları düzeltmek için yeniden başlatmamız gerektiğini belirten bir bildirim görünür. Yeniden başlatıp birkaç saniye beklersek, sorunsuz bir şekilde Windows'a döneceğiz.  

Test sırasında, yukarıda belirtilen sorunlardan bazıları ile nadir de olsa karşılaşıldı. Çok farklı bileşenlere sahip bilgisayarlar olduğundan, sorun çıkma olasılığının unutulmaması ve gerektiğinde başka kurtarma ortamına ihtiyaç duyulabileceği hatırlanmalıdır.  

Günümüzde cep telefonlarımızda genellikle OCR tanıma uygulaması bulunmaktadır. Erişilemeyen ekranlarda neler olduğunu bilmek için kullanılması şiddetle tavsiye edilir.  

Yukarıda belirtildiği gibi, uygulamanın ve eklentinin yazarı, eklenti veya programdan kaynaklanan herhangi bir sorundan dolayı sorumlu tutulamaz.  