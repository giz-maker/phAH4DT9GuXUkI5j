# phAH4DT9GuXUkI5j
 Vadeli Mevduat Açma Kararı
Çalışmada kullanılan veriler herkese açık olan http://archive.ics.uci.edu/ml/datasets adresinden temin edilen veri setine dayandırılmıştır. Bu veri seti, bir Portekiz bankası tarafından belirli bir vadeli mevduat ürününü satmak üzere düzenlenen tele-pazarlama kampanyasının sonuçlarını açıklamaktadır. Veri seti içerisinde ürünün (banka vadeli hesap açma) (‘evet’) veya (‘hayır’) olması durumuna erişmek için, aynı müşteriye birden fazla irtibat yapılması zorunlu tutulmuştur. • Veri seti 41,188 bireysel kayıt içermekte ve her kayıt bir banka müşterisine yapılan bir aramayı temsil etmektedir. • Kronolojik olarak sıralanmış olan veri seti, Mayıs 2008’den Kasım 2010’a kadar olan dönemi kapsamaktadır. • Çağrı merkezi görevlisi, her bir arama kaydı içeren satır için bir vadeli mevduat ürünü satılıp satılmadığını kaydetmiştir. Teknik jargonda, bu karar değişkeni (y-variable) olarak düşünülebilir.

Veri setinde bulunan değişkenler:

age : age of customer (numeric)

job : type of job (categorical)

marital : marital status (categorical)

education (categorical)

default: has credit in default? (binary)

balance: average yearly balance, in euros (numeric)

housing: has a housing loan? (binary)

loan: has personal loan? (binary)

contact: contact communication type (categorical)

day: last contact day of the month (numeric)

month: last contact month of year (categorical)

duration: last contact duration, in seconds (numeric)

campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)

4 farklı model ile eğitim yapılmış olup , en başarılı model olarak acc=0.9125 olan Random Forest Algoritması seçilmiştir. Bonus kısmında ise;

1-)Yatırım ürününü satın alma olasılığı daha yüksek olan müşteriler bulmakla da ilgileniyoruz. Müşterimizin öncelik vermesi gereken müşteri segmentlerini belirleyin.

2-)Müşterilerin satın almasını sağlayan nedir? Bize hangi özelliğe daha fazla odaklanmamız gerektiğini söyleyin.

Sorularına yanıt aranmıştır.