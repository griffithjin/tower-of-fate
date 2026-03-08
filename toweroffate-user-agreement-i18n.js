// js/i18n/user-agreement-i18n.js
// 命运塔用户协议多语言支持

const USER_AGREEMENT_I18N = {
    'zh-CN': {
        title: '用户协议',
        lastUpdated: '最后更新：2026年03月08日',
        sections: {
            welcome: {
                title: '欢迎您使用命运塔！',
                content: '感谢您对《命运塔》（以下简称"本游戏"）的关注与支持。本游戏由命运塔游戏工作室（以下简称"我们"或"开发商"）开发运营。请您在使用本游戏前，仔细阅读并充分理解本协议。'
            },
            ageWarning: {
                title: '年龄提示',
                content: '如果您未满18周岁，请在法定监护人的陪同下阅读本协议，并在取得监护人同意后使用本游戏。'
            },
            account: {
                title: '一、账号管理',
                items: [
                    '您需使用真实有效的身份信息注册账号',
                    '一个手机号/邮箱仅限注册一个游戏账号',
                    '您应妥善保管账号密码',
                    '禁止账号买卖、出租、借用或共享'
                ]
            },
            realName: {
                title: '实名认证',
                content: '根据相关法律法规，您必须完成实名认证方可使用本游戏。未成年人将受到游戏时长和消费限制。'
            },
            virtualItems: {
                title: '二、虚拟物品',
                ownership: '虚拟物品的所有权归我们所有，您获得的是有限的使用许可',
                rules: [
                    '虚拟物品价格以购买时显示为准',
                    '虚拟物品一经购买原则上不予退款',
                    '禁止将虚拟物品用于商业目的'
                ]
            },
            prohibited: {
                title: '三、禁止行为',
                items: [
                    '使用外挂、脚本、作弊器',
                    '利用游戏漏洞获取不正当利益',
                    '账号买卖、出租、借用',
                    '恶意组队、刷分、代练',
                    '发布虚假信息诈骗其他玩家',
                    '侮辱或诽谤其他玩家'
                ]
            },
            minors: {
                title: '四、未成年人保护',
                restrictions: {
                    under8: '未满8周岁：禁止游戏，禁止充值',
                    age8to16: '8-16周岁：每日1小时（节假日2小时），月累计充值≤200元',
                    age16to18: '16-18周岁：每日2小时，月累计充值≤400元'
                }
            },
            privacy: {
                title: '五、隐私保护',
                content: '我们按照《隐私政策》收集、使用和保护您的个人信息。您同意我们收集您的注册信息、游戏数据、设备信息。'
            },
            termination: {
                title: '六、协议终止',
                content: '您可以随时停止使用本游戏并删除账号。删除账号后，您的游戏数据将被清除，已购买的虚拟物品不予退款。'
            },
            contact: {
                title: '七、联系我们',
                email: '客服邮箱：support@tower-of-fate.com',
                phone: '客服电话：400-XXX-XXXX',
                website: '官方网站：https://tower-of-fate.com'
            }
        },
        buttons: {
            agree: '我已阅读并同意',
            disagree: '不同意',
            readFull: '阅读完整协议',
            download: '下载PDF版本'
        },
        warnings: {
            mustAgree: '您必须同意用户协议才能继续',
            ageConfirm: '我已满18周岁或已获得监护人同意'
        }
    },
    
    'en-US': {
        title: 'User Agreement',
        lastUpdated: 'Last Updated: March 8, 2026',
        sections: {
            welcome: {
                title: 'Welcome to Tower of Fate!',
                content: 'Thank you for your interest in "Tower of Fate" (hereinafter referred to as "the Game"). This Game is developed and operated by Tower of Fate Game Studio (hereinafter referred to as "we" or "the Developer"). Please read and fully understand this agreement before using the Game.'
            },
            ageWarning: {
                title: 'Age Notice',
                content: 'If you are under 18 years old, please read this agreement with your legal guardian and use the Game only with their consent.'
            },
            account: {
                title: '1. Account Management',
                items: [
                    'You must register with real and valid identity information',
                    'One phone number/email can only register one game account',
                    'You should keep your account password safe',
                    'Account trading, renting, borrowing, or sharing is prohibited'
                ]
            },
            realName: {
                title: 'Real-Name Verification',
                content: 'According to relevant laws and regulations, you must complete real-name verification to use the Game. Minors will be subject to game time and spending limits.'
            },
            virtualItems: {
                title: '2. Virtual Items',
                ownership: 'Virtual items are owned by us; you are granted a limited license to use them',
                rules: [
                    'Virtual item prices are as displayed at the time of purchase',
                    'Virtual items are generally non-refundable once purchased',
                    'Using virtual items for commercial purposes is prohibited'
                ]
            },
            prohibited: {
                title: '3. Prohibited Behavior',
                items: [
                    'Using cheats, scripts, or hacks',
                    'Exploiting game bugs for unfair advantages',
                    'Account trading, renting, or borrowing',
                    'Teaming, boosting, or account boosting',
                    'Posting false information to scam other players',
                    'Insulting or defaming other players'
                ]
            },
            minors: {
                title: '4. Minor Protection',
                restrictions: {
                    under8: 'Under 8: No gameplay, no purchases',
                    age8to16: 'Ages 8-16: 1 hour/day (2 hours on holidays), monthly spending ≤ $30',
                    age16to18: 'Ages 16-18: 2 hours/day, monthly spending ≤ $60'
                }
            },
            privacy: {
                title: '5. Privacy Protection',
                content: 'We collect, use, and protect your personal information in accordance with our Privacy Policy. You agree that we may collect your registration information, game data, and device information.'
            },
            termination: {
                title: '6. Agreement Termination',
                content: 'You may stop using the Game and delete your account at any time. After account deletion, your game data will be cleared and purchased virtual items will not be refunded.'
            },
            contact: {
                title: '7. Contact Us',
                email: 'Support Email: support@tower-of-fate.com',
                phone: 'Support Phone: +1-XXX-XXX-XXXX',
                website: 'Official Website: https://tower-of-fate.com'
            }
        },
        buttons: {
            agree: 'I have read and agree',
            disagree: 'Disagree',
            readFull: 'Read Full Agreement',
            download: 'Download PDF'
        },
        warnings: {
            mustAgree: 'You must agree to the User Agreement to continue',
            ageConfirm: 'I am 18 or older or have guardian consent'
        }
    },
    
    'ja-JP': {
        title: '利用規約',
        lastUpdated: '最終更新日：2026年3月8日',
        sections: {
            welcome: {
                title: '運命の塔へようこそ！',
                content: '「運命の塔」（以下「本ゲーム」）にご興味をお持ちいただき、ありがとうございます。本ゲームは運命の塔ゲームスタジオ（以下「当社」）によって開発・運営されています。'
            },
            ageWarning: {
                title: '年齢に関する注意',
                content: '18歳未満の方は、法定後見人の同伴のもとで本規約をお読みいただき、同意を得た上で本ゲームをご利用ください。'
            },
            account: {
                title: '1. アカウント管理',
                items: [
                    '真实な身分情報で登録してください',
                    '1つの電話番号/メールアドレスで1つのアカウントのみ登録可能',
                    'アカウントパスワードは適切に管理してください',
                    'アカウントの売買、貸与、借用は禁止されています'
                ]
            },
            realName: {
                title: '実名認証',
                content: '関連法令に基づき、本ゲームを利用するには実名認証が必要です。未成年者にはゲーム時間と課金制限が適用されます。'
            },
            virtualItems: {
                title: '2. 仮想アイテム',
                ownership: '仮想アイテムの所有権は当社にあり、お客様には使用許可が付与されます',
                rules: [
                    '仮想アイテムの価格は購入時の表示通りです',
                    '仮想アイテムは原則として返金できません',
                    '仮想アイテムの商業利用は禁止されています'
                ]
            },
            prohibited: {
                title: '3. 禁止行為',
                items: [
                    'チート、スクリプト、ハックの使用',
                    'ゲームのバグを悪用する行為',
                    'アカウントの売買、貸与',
                    'チームプレイ、ブースティング',
                    '虚偽情報の投稿による詐欺',
                    '他プレイヤーへの侮辱・中傷'
                ]
            },
            minors: {
                title: '4. 未成年者保護',
                restrictions: {
                    under8: '8歳未満：ゲームプレイ・課金禁止',
                    age8to16: '8-16歳：1日1時間（休日2時間）、月額課金≤3000円',
                    age16to18: '16-18歳：1日2時間、月額課金≤6000円'
                }
            },
            privacy: {
                title: '5. プライバシー保護',
                content: '当社はプライバシーポリシーに従って、お客様の個人情報を収集・使用・保護します。'
            },
            termination: {
                title: '6. 規約の終了',
                content: 'お客様はいつでも本ゲームの利用を停止し、アカウントを削除できます。アカウント削除後、ゲームデータは消去され、購入済みの仮想アイテムは返金されません。'
            },
            contact: {
                title: '7. お問い合わせ',
                email: 'サポートメール：support@tower-of-fate.com',
                phone: 'サポート電話：+81-XXX-XXXX',
                website: '公式サイト：https://tower-of-fate.com'
            }
        },
        buttons: {
            agree: '同意します',
            disagree: '同意しません',
            readFull: '全文を読む',
            download: 'PDFをダウンロード'
        },
        warnings: {
            mustAgree: '続行するには利用規約に同意する必要があります',
            ageConfirm: '18歳以上、または後見人の同意を得ています'
        }
    },
    
    'ko-KR': {
        title: '이용약관',
        lastUpdated: '최종 업데이트: 2026년 3월 8일',
        sections: {
            welcome: {
                title: '욕망의 탑에 오신 것을 환영합니다!',
                content: '"욕망의 탑"(이하 "본 게임")에 관심을 가져 주셔서 감사합니다. 본 게임은 욕망의 탑 게임 스튜디오(이하 "당사")에서 개발 및 운영합니다.'
            },
            ageWarning: {
                title: '연령 안내',
                content: '18세 미만인 경우 법정 대리인의 동행 하에 본 약관을 읽고 동의를 얻은 후 본 게임을 이용해 주세요.'
            },
            account: {
                title: '1. 계정 관리',
                items: [
                    '실제 신분 정보로 등록해 주세요',
                    '전화번호/이메일 1개당 계정 1개만 등록 가능',
                    '계정 비밀번호를 안전하게 관리하세요',
                    '계정 거래, 대여, 공유는 금지됩니다'
                ]
            },
            realName: {
                title: '실명 인증',
                content: '관련 법규에 따라 본 게임을 이용하려면 실명 인증이 필요합니다. 미성년자에게는 게임 시간 및 과금 제한이 적용됩니다.'
            },
            virtualItems: {
                title: '2. 가상 아이템',
                ownership: '가상 아이템의 소유권은 당사에 있으며, 사용자에게는 사용 허가가 부여됩니다',
                rules: [
                    '가상 아이템 가격은 구매 시 표시된 가격입니다',
                    '가상 아이템은 원칙적으로 환불되지 않습니다',
                    '가상 아이템의 상업적 이용은 금지됩니다'
                ]
            },
            prohibited: {
                title: '3. 금지 행위',
                items: [
                    '치트, 스크립트, 핵 사용',
                    '게임 버그 악용',
                    '계정 거래, 대여',
                    '팀플레이, 부스팅',
                    '허위 정보 게시를 통한 사기',
                    '다른 플레이어 모욕/명예훼손'
                ]
            },
            minors: {
                title: '4. 미성년자 보호',
                restrictions: {
                    under8: '8세 미만: 게임 플레이 및 과금 금지',
                    age8to16: '8-16세: 1일 1시간(휴일 2시간), 월 과금 ≤ 30,000원',
                    age16to18: '16-18세: 1일 2시간, 월 과금 ≤ 60,000원'
                }
            },
            privacy: {
                title: '5. 개인정보 보호',
                content: '당사는 개인정보처리방침에 따라 귀하의 개인정보를 수집, 사용, 보호합니다.'
            },
            termination: {
                title: '6. 약관 종료',
                content: '귀하는 언제든지 본 게임 이용을 중단하고 계정을 삭제할 수 있습니다. 계정 삭제 후 게임 데이터는 삭제되며 구매한 가상 아이템은 환불되지 않습니다.'
            },
            contact: {
                title: '7. 문의하기',
                email: '고객지원 이메일: support@tower-of-fate.com',
                phone: '고객지원 전화: +82-XXX-XXXX',
                website: '공식 웹사이트: https://tower-of-fate.com'
            }
        },
        buttons: {
            agree: '동의합니다',
            disagree: '동의하지 않습니다',
            readFull: '전문 읽기',
            download: 'PDF 다운로드'
        },
        warnings: {
            mustAgree: '계속하려면 이용약관에 동의해야 합니다',
            ageConfirm: '18세 이상이거나 보호자 동의를 받았습니다'
        }
    },
    
    // 德语
    'de-DE': {
        title: 'Nutzungsbedingungen',
        lastUpdated: 'Zuletzt aktualisiert: 8. März 2026',
        sections: {
            welcome: {
                title: 'Willkommen bei Tower of Fate!',
                content: 'Vielen Dank für Ihr Interesse an "Tower of Fate" (im Folgenden "das Spiel" genannt). Dieses Spiel wird vom Tower of Fate Game Studio (im Folgenden "wir") entwickelt und betrieben.'
            },
            ageWarning: {
                title: 'Altersinformation',
                content: 'Wenn Sie unter 18 Jahre alt sind, lesen Sie diese Vereinbarung bitte in Begleitung Ihres gesetzlichen Vormunds und nutzen Sie das Spiel nur mit dessen Zustimmung.'
            },
            account: {
                title: '1. Kontoverwaltung',
                items: [
                    'Registrieren Sie sich mit echten Identitätsinformationen',
                    'Eine Telefonnummer/E-Mail kann nur ein Konto registrieren',
                    'Verwahren Sie Ihr Passwort sicher',
                    'Kontenhandel, -verleih oder -freigabe ist verboten'
                ]
            },
            minors: {
                title: '4. Jugendschutz',
                restrictions: {
                    under8: 'Unter 8 Jahren: Kein Spielen, keine Käufe',
                    age8to16: '8-16 Jahre: 1 Stunde/Tag (2 Stunden an Feiertagen), monatliche Ausgaben ≤ 25€',
                    age16to18: '16-18 Jahre: 2 Stunden/Tag, monatliche Ausgaben ≤ 50€'
                }
            }
        },
        buttons: {
            agree: 'Ich stimme zu',
            disagree: 'Ablehnen',
            readFull: 'Vollständige Bedingungen lesen',
            download: 'PDF herunterladen'
        },
        warnings: {
            mustAgree: 'Sie müssen den Nutzungsbedingungen zustimmen, um fortzufahren',
            ageConfirm: 'Ich bin 18 oder älter oder habe die Zustimmung eines Vormunds'
        }
    },
    
    // 法语
    'fr-FR': {
        title: 'Conditions d\'utilisation',
        lastUpdated: 'Dernière mise à jour : 8 mars 2026',
        sections: {
            welcome: {
                title: 'Bienvenue dans Tower of Fate !',
                content: 'Merci de votre intérêt pour "Tower of Fate" (ci-après "le Jeu"). Ce jeu est développé et exploité par Tower of Fate Game Studio (ci-après "nous").'
            },
            ageWarning: {
                title: 'Information sur l\'âge',
                content: 'Si vous avez moins de 18 ans, veuillez lire cet accord accompagné de votre tuteur légal et n\'utiliser le Jeu qu\'avec son consentement.'
            },
            minors: {
                title: '4. Protection des mineurs',
                restrictions: {
                    under8: 'Moins de 8 ans : Pas de jeu, pas d\'achats',
                    age8to16: '8-16 ans : 1 heure/jour (2 heures les jours fériés), dépenses mensuelles ≤ 25€',
                    age16to18: '16-18 ans : 2 heures/jour, dépenses mensuelles ≤ 50€'
                }
            }
        },
        buttons: {
            agree: 'J\'accepte',
            disagree: 'Refuser',
            readFull: 'Lire les conditions complètes',
            download: 'Télécharger le PDF'
        },
        warnings: {
            mustAgree: 'Vous devez accepter les conditions d\'utilisation pour continuer',
            ageConfirm: 'J\'ai 18 ans ou plus ou j\'ai le consentement d\'un tuteur'
        }
    },
    
    // 西班牙语
    'es-ES': {
        title: 'Términos de uso',
        lastUpdated: 'Última actualización: 8 de marzo de 2026',
        sections: {
            welcome: {
                title: '¡Bienvenido a Tower of Fate!',
                content: 'Gracias por su interés en "Tower of Fate" (en adelante "el Juego"). Este juego es desarrollado y operado por Tower of Fate Game Studio (en adelante "nosotros").'
            },
            ageWarning: {
                title: 'Información de edad',
                content: 'Si tiene menos de 18 años, lea este acuerdo acompañado de su tutor legal y use el Juego solo con su consentimiento.'
            },
            minors: {
                title: '4. Protección de menores',
                restrictions: {
                    under8: 'Menores de 8 años: Sin juego, sin compras',
                    age8to16: '8-16 años: 1 hora/día (2 horas en festivos), gasto mensual ≤ 25€',
                    age16to18: '16-18 años: 2 horas/día, gasto mensual ≤ 50€'
                }
            }
        },
        buttons: {
            agree: 'Acepto',
            disagree: 'Rechazar',
            readFull: 'Leer términos completos',
            download: 'Descargar PDF'
        },
        warnings: {
            mustAgree: 'Debe aceptar los términos de uso para continuar',
            ageConfirm: 'Tengo 18 años o más o tengo consentimiento de un tutor'
        }
    },
    
    // 葡萄牙语
    'pt-BR': {
        title: 'Termos de uso',
        lastUpdated: 'Última atualização: 8 de março de 2026',
        sections: {
            welcome: {
                title: 'Bem-vindo ao Tower of Fate!',
                content: 'Obrigado pelo seu interesse em "Tower of Fate" (doravante "o Jogo"). Este jogo é desenvolvido e operado pela Tower of Fate Game Studio (doravante "nós").'
            },
            minors: {
                title: '4. Proteção de menores',
                restrictions: {
                    under8: 'Menos de 8 anos: Sem jogo, sem compras',
                    age8to16: '8-16 anos: 1 hora/dia (2 horas em feriados), gasto mensal ≤ R$150',
                    age16to18: '16-18 anos: 2 horas/dia, gasto mensal ≤ R$300'
                }
            }
        },
        buttons: {
            agree: 'Concordo',
            disagree: 'Recusar',
            readFull: 'Ler termos completos',
            download: 'Baixar PDF'
        },
        warnings: {
            mustAgree: 'Você deve concordar com os termos de uso para continuar',
            ageConfirm: 'Tenho 18 anos ou mais ou tenho consentimento de um tutor'
        }
    },
    
    // 俄语
    'ru-RU': {
        title: 'Пользовательское соглашение',
        lastUpdated: 'Последнее обновление: 8 марта 2026 г.',
        sections: {
            welcome: {
                title: 'Добро пожаловать в Tower of Fate!',
                content: 'Благодарим вас за интерес к "Tower of Fate" (далее "Игра"). Эта игра разработана и управляется студией Tower of Fate Game Studio (далее "мы").'
            },
            minors: {
                title: '4. Защита несовершеннолетних',
                restrictions: {
                    under8: 'До 8 лет: Игра и покупки запрещены',
                    age8to16: '8-16 лет: 1 час/день (2 часа в праздники), расходы ≤ 2500₽',
                    age16to18: '16-18 лет: 2 часа/день, расходы ≤ 5000₽'
                }
            }
        },
        buttons: {
            agree: 'Согласен',
            disagree: 'Отказаться',
            readFull: 'Прочитать полные условия',
            download: 'Скачать PDF'
        },
        warnings: {
            mustAgree: 'Вы должны согласиться с условиями использования для продолжения',
            ageConfirm: 'Мне 18 лет или больше, или у меня есть согласие опекуна'
        }
    },
    
    // 阿拉伯语
    'ar-SA': {
        title: 'اتفاقية المستخدم',
        lastUpdated: 'آخر تحديث: 8 مارس 2026',
        sections: {
            welcome: {
                title: 'مرحبًا بك في Tower of Fate!',
                content: 'شكرًا لاهتمامك بـ "Tower of Fate" (以下简称 "اللعبة"). هذه اللعبة مطورة ومدارة بواسطة Tower of Fate Game Studio (以下简称 "نحن").'
            },
            minors: {
                title: '4. حماية القصر',
                restrictions: {
                    under8: 'أقل من 8 سنوات: ممنوع اللعب والشراء',
                    age8to16: '8-16 سنة: ساعة واحدة/يوم (ساعتان في العطل)، الإنفاق ≤ 100 ريال',
                    age16to18: '16-18 سنة: ساعتان/يوم، الإنفاق ≤ 200 ريال'
                }
            }
        },
        buttons: {
            agree: 'أوافق',
            disagree: 'رفض',
            readFull: 'قراءة الشروط الكاملة',
            download: 'تحميل PDF'
        },
        warnings: {
            mustAgree: 'يجب الموافقة على شروط الاستخدام للمتابعة',
            ageConfirm: 'عمري 18 سنة أو أكثر ولدي موافقة ولي الأمر'
        }
    },
    
    // 印地语
    'hi-IN': {
        title: 'उपयोगकर्ता अनुबंध',
        lastUpdated: 'अंतिम अपडेट: 8 मार्च 2026',
        sections: {
            welcome: {
                title: 'Tower of Fate में आपका स्वागत है!',
                content: '"Tower of Fate" (hereinafter "the Game") में आपकी रुचि के लिए धन्यवाद। यह गेम Tower of Fate Game Studio (hereinafter "we") द्वारा विकसित और संचालित है।'
            },
            minors: {
                title: '4. नाबालिगों का संरक्षण',
                restrictions: {
                    under8: '8 साल से कम: कोई गेम, कोई खरीदारी नहीं',
                    age8to16: '8-16 साल: 1 घंटा/दिन (छुट्टियों में 2 घंटे), मासिक खर्च ≤ ₹2000',
                    age16to18: '16-18 साल: 2 घंटे/दिन, मासिक खर्च ≤ ₹4000'
                }
            }
        },
        buttons: {
            agree: 'मैं सहमत हूँ',
            disagree: 'अस्वीकार करें',
            readFull: 'पूर्ण शर्तें पढ़ें',
            download: 'PDF डाउनलोड करें'
        },
        warnings: {
            mustAgree: 'जारी रखने के लिए आपको उपयोग की शर्तों से सहमत होना होगा',
            ageConfirm: 'मेरी उम्र 18 साल या उससे अधिक है या मुझे अभिभावक की सहमति है'
        }
    },
    
    // 泰语
    'th-TH': {
        title: 'ข้อตกลงผู้ใช้',
        lastUpdated: 'อัปเดตล่าสุด: 8 มีนาคม 2026',
        sections: {
            welcome: {
                title: 'ยินดีต้อนรับสู่ Tower of Fate!',
                content: 'ขอบคุณที่สนใจ "Tower of Fate" (ต่อไปนี้ "เกม") เกมนี้พัฒนาและดำเนินการโดย Tower of Fate Game Studio (ต่อไปนี้ "เรา")'
            },
            minors: {
                title: '4. การคุ้มครองผู้เยาว์',
                restrictions: {
                    under8: 'อายุต่ำกว่า 8 ปี: ห้ามเล่นเกมและซื้อของ',
                    age8to16: '8-16 ปี: 1 ชั่วโมง/วัน (2 ชั่วโมงในวันหยุด), ค่าใช้จ่ายรายเดือน ≤ 1,000 บาท',
                    age16to18: '16-18 ปี: 2 ชั่วโมง/วัน, ค่าใช้จ่ายรายเดือน ≤ 2,000 บาท'
                }
            }
        },
        buttons: {
            agree: 'ฉันยอมรับ',
            disagree: 'ปฏิเสธ',
            readFull: 'อ่านข้อกำหนดฉบับเต็ม',
            download: 'ดาวน์โหลด PDF'
        },
        warnings: {
            mustAgree: 'คุณต้องยอมรับข้อกำหนดในการใช้งานเพื่อดำเนินการต่อ',
            ageConfirm: 'ฉันอายุ 18 ปีขึ้นไป หรือได้รับความยินยอมจากผู้ปกครอง'
        }
    },
    
    // 越南语
    'vi-VN': {
        title: 'Thỏa thuận ngườii dùng',
        lastUpdated: 'Cập nhật lần cuối: 8 tháng 3 năm 2026',
        sections: {
            welcome: {
                title: 'Chào mừng đến với Tower of Fate!',
                content: 'Cảm ơn bạn đã quan tâm đến "Tower of Fate" (sau đây gọi là "Trò chơi"). Trò chơi này được phát triển và vận hành bởi Tower of Fate Game Studio (sau đây gọi là "chúng tôi").'
            },
            minors: {
                title: '4. Bảo vệ ngườii chưa thành niên',
                restrictions: {
                    under8: 'Dưới 8 tuổi: Không chơi game, không mua hàng',
                    age8to16: '8-16 tuổi: 1 giờ/ngày (2 giờ vào ngày lễ), chi tiêu tháng ≤ 700,000đ',
                    age16to18: '16-18 tuổi: 2 giờ/ngày, chi tiêu tháng ≤ 1,400,000đ'
                }
            }
        },
        buttons: {
            agree: 'Tôi đồng ý',
            disagree: 'Từ chối',
            readFull: 'Đọc điều khoản đầy đủ',
            download: 'Tải xuống PDF'
        },
        warnings: {
            mustAgree: 'Bạn phải đồng ý với điều khoản sử dụng để tiếp tục',
            ageConfirm: 'Tôi đã 18 tuổi trở lên hoặc có sự đồng ý của ngườii giám hộ'
        }
    },
    
    // 印尼语
    'id-ID': {
        title: 'Perjanjian Pengguna',
        lastUpdated: 'Terakhir diperbarui: 8 Maret 2026',
        sections: {
            welcome: {
                title: 'Selamat datang di Tower of Fate!',
                content: 'Terima kasih atas minat Anda pada "Tower of Fate" (selanjutnya "Permainan"). Permainan ini dikembangkan dan dioperasikan oleh Tower of Fate Game Studio (selanjutnya "kami").'
            },
            minors: {
                title: '4. Perlindungan Anak',
                restrictions: {
                    under8: 'Di bawah 8 tahun: Tidak bermain, tidak membeli',
                    age8to16: '8-16 tahun: 1 jam/hari (2 jam di hari libur), pengeluaran bulanan ≤ Rp500.000',
                    age16to18: '16-18 tahun: 2 jam/hari, pengeluaran bulanan ≤ Rp1.000.000'
                }
            }
        },
        buttons: {
            agree: 'Saya setuju',
            disagree: 'Tolak',
            readFull: 'Baca syarat lengkap',
            download: 'Unduh PDF'
        },
        warnings: {
            mustAgree: 'Anda harus menyetujui syarat penggunaan untuk melanjutkan',
            ageConfirm: 'Saya berusia 18 tahun atau lebih atau memiliki persetujuan wali'
        }
    },
    
    // 土耳其语
    'tr-TR': {
        title: 'Kullanıcı Sözleşmesi',
        lastUpdated: 'Son güncelleme: 8 Mart 2026',
        sections: {
            welcome: {
                title: 'Tower of Fate\'e Hoş Geldiniz!',
                content: '"Tower of Fate" (bundan böyle "Oyun") ilginiz için teşekkür ederiz. Bu oyun Tower of Fate Game Studio (bundan böyle "biz") tarafından geliştirilmiş ve işletilmektedir.'
            },
            minors: {
                title: '4. Küçüklerin Korunması',
                restrictions: {
                    under8: '8 yaş altı: Oyun ve satın alma yasak',
                    age8to16: '8-16 yaş: Günde 1 saat (tatillerde 2 saat), aylık harcama ≤ 400₺',
                    age16to18: '16-18 yaş: Günde 2 saat, aylık harcama ≤ 800₺'
                }
            }
        },
        buttons: {
            agree: 'Kabul ediyorum',
            disagree: 'Reddet',
            readFull: 'Tam koşulları oku',
            download: 'PDF indir'
        },
        warnings: {
            mustAgree: 'Devam etmek için kullanım koşullarını kabul etmelisiniz',
            ageConfirm: '18 yaşındayım veya daha büyüğüm veya bir velinin onayına sahibim'
        }
    }
};

// 用户协议管理器
class UserAgreementManager {
    constructor() {
        this.currentLang = localStorage.getItem('user-agreement-lang') || 'zh-CN';
        this.agreedVersions = JSON.parse(localStorage.getItem('agreed-versions') || '{}');
    }
    
    // 获取当前语言版本
    getAgreement(lang = this.currentLang) {
        return USER_AGREEMENT_I18N[lang] || USER_AGREEMENT_I18N['en-US'];
    }
    
    // 切换语言
    setLanguage(lang) {
        this.currentLang = lang;
        localStorage.setItem('user-agreement-lang', lang);
    }
    
    // 检查是否需要显示协议
    needShowAgreement() {
        const currentVersion = '1.0'; // 当前协议版本
        const lastAgreed = this.agreedVersions[this.currentLang];
        return !lastAgreed || lastAgreed !== currentVersion;
    }
    
    // 记录同意
    agree(version = '1.0') {
        this.agreedVersions[this.currentLang] = version;
        localStorage.setItem('agreed-versions', JSON.stringify(this.agreedVersions));
        localStorage.setItem(`agreed-at-${this.currentLang}`, new Date().toISOString());
    }
    
    // 渲染协议弹窗
    renderAgreementModal() {
        const agreement = this.getAgreement();
        
        return `
            <div id="user-agreement-modal" class="agreement-modal">
                <div class="agreement-content">
                    <div class="agreement-header">
                        <h2>${agreement.title}</h2>
                        <p class="last-updated">${agreement.lastUpdated}</p>
                        <div class="language-selector">
                            <select id="agreement-lang-select" onchange="userAgreementManager.changeLanguage(this.value)">
                                <option value="zh-CN" ${this.currentLang === 'zh-CN' ? 'selected' : ''}>中文</option>
                                <option value="en-US" ${this.currentLang === 'en-US' ? 'selected' : ''}>English</option>
                                <option value="ja-JP" ${this.currentLang === 'ja-JP' ? 'selected' : ''}>日本語</option>
                                <option value="ko-KR" ${this.currentLang === 'ko-KR' ? 'selected' : ''}>한국어</option>
                                <option value="de-DE" ${this.currentLang === 'de-DE' ? 'selected' : ''}>Deutsch</option>
                                <option value="fr-FR" ${this.currentLang === 'fr-FR' ? 'selected' : ''}>Français</option>
                                <option value="es-ES" ${this.currentLang === 'es-ES' ? 'selected' : ''}>Español</option>
                                <option value="pt-BR" ${this.currentLang === 'pt-BR' ? 'selected' : ''}>Português</option>
                                <option value="ru-RU" ${this.currentLang === 'ru-RU' ? 'selected' : ''}>Русский</option>
                                <option value="ar-SA" ${this.currentLang === 'ar-SA' ? 'selected' : ''}>العربية</option>
                                <option value="hi-IN" ${this.currentLang === 'hi-IN' ? 'selected' : ''}>हिन्दी</option>
                                <option value="th-TH" ${this.currentLang === 'th-TH' ? 'selected' : ''}>ไทย</option>
                                <option value="vi-VN" ${this.currentLang === 'vi-VN' ? 'selected' : ''}>Tiếng Việt</option>
                                <option value="id-ID" ${this.currentLang === 'id-ID' ? 'selected' : ''}>Bahasa Indonesia</option>
                                <option value="tr-TR" ${this.currentLang === 'tr-TR' ? 'selected' : ''}>Türkçe</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="agreement-body">
                        <section class="agreement-section">
                            <h3>${agreement.sections.welcome.title}</h3>
                            <p>${agreement.sections.welcome.content}</p>
                        </section>
                        
                        <section class="agreement-section warning">
                            <h3>${agreement.sections.ageWarning.title}</h3>
                            <p>${agreement.sections.ageWarning.content}</p>
                        </section>
                        
                        <section class="agreement-section">
                            <h3>${agreement.sections.account.title}</h3>
                            <ul>
                                ${agreement.sections.account.items.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        </section>
                        
                        <section class="agreement-section">
                            <h3>${agreement.sections.virtualItems.title}</h3>
                            <p><strong>${agreement.sections.virtualItems.ownership}</strong></p>
                            <ul>
                                ${agreement.sections.virtualItems.rules.map(rule => `<li>${rule}</li>`).join('')}
                            </ul>
                        </section>
                        
                        <section class="agreement-section">
                            <h3>${agreement.sections.prohibited.title}</h3>
                            <ul>
                                ${agreement.sections.prohibited.items.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        </section>
                        
                        <section class="agreement-section important">
                            <h3>${agreement.sections.minors.title}</h3>
                            <div class="minors-restrictions">
                                <div class="restriction-item">
                                    <span class="age">&lt; 8</span>
                                    <span>${agreement.sections.minors.restrictions.under8}</span>
                                </div>
                                <div class="restriction-item">
                                    <span class="age">8-16</span>
                                    <span>${agreement.sections.minors.restrictions.age8to16}</span>
                                </div>
                                <div class="restriction-item">
                                    <span class="age">16-18</span>
                                    <span>${agreement.sections.minors.restrictions.age16to18}</span>
                                </div>
                            </div>
                        </section>
                        
                        <section class="agreement-section">
                            <h3>${agreement.sections.privacy.title}</h3>
                            <p>${agreement.sections.privacy.content}</p>
                        </section>
                        
                        <section class="agreement-section">
                            <h3>${agreement.sections.contact.title}</h3>
                            <p>${agreement.sections.contact.email}</p>
                            <p>${agreement.sections.contact.phone}</p>
                            <p>${agreement.sections.contact.website}</p>
                        </section>
                    </div>
                    
                    <div class="agreement-footer">
                        <label class="age-confirm">
                            <input type="checkbox" id="age-confirm-checkbox">
                            <span>${agreement.warnings.ageConfirm}</span>
                        </label>
                        
                        <div class="agreement-actions">
                            <button class="btn-secondary" onclick="userAgreementManager.decline()">
                                ${agreement.buttons.disagree}
                            </button>
                            <button class="btn-primary" id="agree-btn" onclick="userAgreementManager.accept()" disabled>
                                ${agreement.buttons.agree}
                            </button>
                        </div>
                        
                        <div class="agreement-links">
                            <a href="#" onclick="userAgreementManager.showFullAgreement()">${agreement.buttons.readFull}</a>
                            <a href="#" onclick="userAgreementManager.downloadPDF()">${agreement.buttons.download}</a>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // 切换语言
    changeLanguage(lang) {
        this.setLanguage(lang);
        document.getElementById('user-agreement-modal').outerHTML = this.renderAgreementModal();
        this.attachEventListeners();
    }
    
    // 附加事件监听
    attachEventListeners() {
        const checkbox = document.getElementById('age-confirm-checkbox');
        const agreeBtn = document.getElementById('agree-btn');
        
        if (checkbox && agreeBtn) {
            checkbox.addEventListener('change', (e) => {
                agreeBtn.disabled = !e.target.checked;
            });
        }
    }
    
    // 接受协议
    accept() {
        const checkbox = document.getElementById('age-confirm-checkbox');
        if (!checkbox.checked) {
            const agreement = this.getAgreement();
            alert(agreement.warnings.mustAgree);
            return;
        }
        
        this.agree();
        document.getElementById('user-agreement-modal').remove();
        
        // 触发同意事件
        window.dispatchEvent(new CustomEvent('userAgreementAccepted', { 
            detail: { lang: this.currentLang } 
        }));
    }
    
    // 拒绝协议
    decline() {
        // 显示提示并退出
        const agreement = this.getAgreement();
        if (confirm(agreement.warnings.mustAgree)) {
            // 可以重定向到退出页面或关闭游戏
            window.location.href = 'about:blank';
        }
    }
    
    // 显示完整协议
    showFullAgreement() {
        window.open(`/docs/user-agreement-${this.currentLang}.html`, '_blank');
    }
    
    // 下载PDF
    downloadPDF() {
        window.open(`/docs/user-agreement-${this.currentLang}.pdf`, '_blank');
    }
    
    // 初始化
    init() {
        if (this.needShowAgreement()) {
            const modalHTML = this.renderAgreementModal();
            document.body.insertAdjacentHTML('beforeend', modalHTML);
            this.attachEventListeners();
        }
    }
}

// 创建全局实例
const userAgreementManager = new UserAgreementManager();

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', () => {
    userAgreementManager.init();
});

// 导出
window.USER_AGREEMENT_I18N = USER_AGREEMENT_I18N;
window.UserAgreementManager = UserAgreementManager;
window.userAgreementManager = userAgreementManager;
