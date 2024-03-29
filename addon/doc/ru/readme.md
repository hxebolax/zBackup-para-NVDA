# Руководство zBackup для NVDA.

zBackup позволит нам создавать резервные копии раздела, содержащего операционную систему.

Это означает, что диск или раздел, содержащий установку Windows, могут быть сохранены для восстановления.

zBackup может делать горячие резервные копии без остановки приложений или прекратить делать то, что мы делаем.

[Этот плагин основан на приложении Drive Snapshot.](http://www.drivesnapshot.de/en/index.htm)

zBackup 
это упрощает общие и необходимые действия, чтобы мы могли создавать резервные копии и восстанавливать их без помощи или внешних инструментов, таких как WinPE.

Помимо резервного копирования, мы можем восстановить эти копии, смонтировать их как виртуальные диски и все это доступным способом.

zBackup основан на Drive Snapshot, поэтому он использует приложение, внешнее для NVDA. Это приложение весит менее 500 КБ и будет загружено с официального сайта, когда мы запустим плагин 
впервые. При каждом обновлении плагина zBackup приложение будет загружено со своей страницы, чтобы всегда иметь последнюю версию.

Drive SnapShot не является бесплатным приложением и имеет свои ограничения. Приложение можно использовать в течение 30 дней в полном объеме, но по прошествии этого времени единственное, что вы не оставите, это продолжать создавать резервные копии, хотя и восстанавливать и монтировать их.

На странице приложения мы можем купить Drive SnapShot за 39 евро по самой базовой лицензии, 
достаточно для личного использования.

Если лицензия приобретена, имейте в виду, что мы должны иметь ее под рукой и хорошо сохранены, потому что каждый раз, когда мы обновляем zBackup, при загрузке обновленной версии приложения, мы должны зарегистрировать ее, чтобы иметь неограниченное время.

## * * * Очень важная информация ***

zBackup был протестирован в различных условиях и ситуациях с отличными результатами. Однако в компьютерном мире все может случиться, и могут быть сбои, так что это 
дополнение рекомендуется только для людей с достаточными знаниями, чтобы выйти из плохого восстановления системы. Это означает, что вы знаете, как загрузиться с другого носителя, чтобы получить информацию, установить операционную систему и, в конечном счете, иметь возможность снова иметь Windows, если что-то пошло не так.

При использовании плагина пользователь несет единоличную ответственность за результаты, исключая автора приложения и плагина из любых проблем, которые могут возникнуть в отношении 
плохое восстановление, неисправное резервное копирование, частичная или полная потеря данных и, в конечном счете, конечный результат использования такого пакета.

## * * * Предупреждение для хорошего использования ***

zBackup включает в себя средства защиты, чтобы избежать ошибок, такие как восстановление из того же раздела Windows, использование недопустимых символов в именах копий, защита от нехватки места и т. д. Однако необходимо учитывать несколько соображений.

Резервные копии могут быть только 
восстановление с другого раздела или диска, чем Windows. Копии также могут быть восстановлены с внешних носителей, но мы должны учитывать скорость чтения таких носителей. Медленный носитель может вызвать проблемы при восстановлении, поэтому рекомендуется использовать внешние диски SSD или какой-либо высокоскоростной метод хранения USB Type-C.

Следует отметить, что если мы создадим резервную копию BIOS в небезопасном режиме, мы сможем восстановить ее 
копируйте, пока мы в этом режиме. Если мы переключимся в безопасный режим, копия, сделанная в небезопасном режиме, больше не будет восстановлена. Каждая копия должна быть восстановлена с соответствующим оборудованием и соответствующей конфигурацией оборудования.

Кроме того, рекомендуется не использовать zBackup для резервного копирования дисков, защищенных BitLocker.

zBackup был протестирован на Windows 10 и 11, но действителен на Windows 7 и 8 в соответствии с документацией приложения.

Рекомендуется, чтобы каталог 
там, где мы храним резервные копии, не содержится пробелов.

zBackup не может использоваться из переносимых копий NVDA.

## Интерфейс zBackup

zBackup стремится иметь несколько вариантов и быть ясным, поэтому во все времена он будет давать нам информационные сообщения о том, что он будет делать и шаги, чтобы следовать.

На главном экране вы можете сделать резервную копию.

Для запуска главного экрана вам нужно добавить жест в NVDA / настройки / жесты ввода / категории zBackup.

Один раз 
открыв, мы попадем в поле только для чтения, которое будет содержать каталог, в котором мы сохраним резервную копию. Если мы введем табуляцию, мы попадем на кнопку выбрать каталог, которая позволит нам выбрать этот каталог.

Резервные копии будут сохранены в подпапках в этом каталоге. Рекомендуется, чтобы в этой папке не было пробелов.

Если мы снова введем табуляцию, мы попадем в поле редактирования с именем Имя для резервного копирования. В этом поле мы поместим идентификационное имя 
из нашей резервной копии.

В этом поле в папках и файлах не разрешены пробелы или символы, не разрешенные Windows. Эти символы заключаются в тройных кавычках:

"""\ / : * ? » < > |"""

Это идентификационное имя будет использоваться для именования подпапки и различных файлов в резервной копии.

Если мы вернемся в таблицу, мы попадем в поле со списком, где мы сможем выбрать размер каждого файла в резервной копии. Мы можем выбрать 
от 500 МБ до 10 ГБ.

Это означает, что при резервном копировании полученные файлы будут иметь такой размер. Чтобы привести пример: если наш раздел Windows имеет размер около 60 ГБ, полученная копия будет иметь общий размер от 20 до 30 ГБ. Если мы выберем, чтобы полученные файлы были 10 ГБ, он создаст около 3 файлов.

Если мы снова введем табуляцию, мы попадем на кнопку Начать резервное копирование. Если все данные хорошо заполнены и 
условия пространства и местоположения, даст нам возможность начать резервное копирование, заявив, что вы будете делать в любое время.

Если мы вернемся к табличке, мы попадем на кнопку Меню. Если мы нажмем на него, появится контекстное меню со следующими параметрами:

* Восстановление резервной копии: с помощью этой опции вы сможете восстановить резервную копию. Мы будем ориентироваться с сообщениями. Важно отметить, что, как только вы достигнете точки выбора изображения для восстановления и принятия его, 
процесс больше не имеет пути назад, и система будет восстановлена.

* Смонтировать виртуальный диск из резервной копии: с помощью этой опции у нас будет возможность выбрать свободный диск с нашего компьютера и смонтировать практически копию. Это хорошо, если у нас есть что-то конкретное, что мы хотим восстановить из копии, и мы не хотим полностью восстанавливать.

* Отключить виртуальные диски: этот параметр отключит все виртуальные диски, которые мы смонтировали с помощью zBackup. Невозможно выбрать а 
одно. Эта опция будет работать успешно, даже если у нас ее нет.

* Запустите приложение Drive Snapshot: с помощью этой опции мы запустим Drive Snapshot и сможем использовать приложение в режиме графического интерфейса. Мы также можем зарегистрировать его с помощью serial, если вы приобрели лицензию.

Все элементы управления имеют сочетания клавиш, которые сообщаются в соответствии с интерфейсом.

## Другие

При резервном копировании необходимо, чтобы диск или раздел 
цель имеет размер системного раздела. Если системный раздел имеет 60 ГБ, необходимо иметь свободный 60 ГБ в целевом разделе, даже если тогда копия занимает половину или меньше. Это для безопасности.

Желательно иметь загрузочный носитель на случай, если что-то пойдет не так. Рекомендуется использовать WinPE и Drive Snapshot на таком носителе. Таким образом, мы могли бы восстановить из резервной копии систему.

zBackup был протестирован на Windows, без изменений. Не гарантируется бесперебойная работа в 
некоторые измененные версии Windows, циркулирующие в Интернете.

Я снова предупреждаю, что zBackup не будет использоваться, если у вас нет знаний, чтобы выйти из плохого восстановления.

## Найденные проблемы

Плагин был протестирован на нескольких компьютерах с различным оборудованием и конфигурацией, а также на виртуальных машинах.

Когда он загружается для восстановления, мы можем иметь в качестве руководства, что вентиляторы компьютера приступают к работе и останавливаются, когда восстановление заканчивается. 
Точно так же, если у нас есть подключенные наушники, с помощью щелчков в наушниках мы можем обнаружить перезагрузки.

В безопасном режиме иногда после восстановления резервной копии система не загружается и остается на логотипе производителя.

В таких случаях желательно подождать несколько минут и выключить компьютер.

При следующем запуске Windows спросит нас, хотим ли мы выполнить проверку диска или начать эту проверку самостоятельно, что приведет к недоступному экрану 
это говорит нам попробовать другой вариант, чтобы восстановить или выключить компьютер.

Если мы нажмем Enter, он выключится. В следующий раз, когда мы загрузим компьютер, он загрузится в Windows.

Это защита безопасного режима, который хила очень хорошо, но на самом деле восстановление было сделано правильно.

Точно так же он иногда загружается в Windows, и когда мы уже входим в систему, появляется уведомление о том, что нам нужно перезагрузиться, чтобы исправить ошибки. Если мы перезагрузимся и подождем несколько секунд, мы вернемся 
в Windows, уже без каких-либо проблем.

Во время испытаний это случалось когда-то, в меньшинстве раз. Тем не менее, это может произойти, поэтому вы должны знать, что это сделано. Уведомление о наличии другого средства восстановления на всякий случай остается в силе, и понимание того, что есть сотни машин, конфигураций, и то, что работает на одном, может не работать на другом.

Сегодня у нас обычно есть приложение распознавания OCR на наших мобильных устройствах. Настоятельно рекомендуется использовать его, чтобы знать, что 
это происходит на недоступных экранах.

Как отмечалось выше, автор приложения и плагина освобождается от ответственности за любые проблемы, вызванные плагином или программой.

### Перевод

* Русский: Валентин Куприянов.
