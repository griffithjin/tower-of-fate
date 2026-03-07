/**
 * Tower3DConfigs - 196个塔的3D配置数据
 * 每个塔13层结构，支持4种模板类型
 */

import SphereTowerTemplate from './tower-templates/template-sphere.js';
import LatticeTowerTemplate from './tower-templates/template-lattice.js';
import PyramidTowerTemplate from './tower-templates/template-pyramid.js';
import ModernTowerTemplate from './tower-templates/template-modern.js';

// 模板映射
const TEMPLATES = {
    sphere: SphereTowerTemplate,
    lattice: LatticeTowerTemplate,
    pyramid: PyramidTowerTemplate,
    modern: ModernTowerTemplate
};

// 196个国家的塔配置
const COUNTRY_TOWERS = [
    // A开头国家
    { code: 'AF', name: '阿富汗', nameEn: 'Afghanistan', template: 'pyramid' },
    { code: 'AL', name: '阿尔巴尼亚', nameEn: 'Albania', template: 'modern' },
    { code: 'DZ', name: '阿尔及利亚', nameEn: 'Algeria', template: 'pyramid' },
    { code: 'AD', name: '安道尔', nameEn: 'Andorra', template: 'modern' },
    { code: 'AO', name: '安哥拉', nameEn: 'Angola', template: 'modern' },
    { code: 'AR', name: '阿根廷', nameEn: 'Argentina', template: 'lattice' },
    { code: 'AM', name: '亚美尼亚', nameEn: 'Armenia', template: 'modern' },
    { code: 'AU', name: '澳大利亚', nameEn: 'Australia', template: 'modern' },
    { code: 'AT', name: '奥地利', nameEn: 'Austria', template: 'modern' },
    { code: 'AZ', name: '阿塞拜疆', nameEn: 'Azerbaijan', template: 'modern' },
    
    // B开头国家
    { code: 'BS', name: '巴哈马', nameEn: 'Bahamas', template: 'sphere' },
    { code: 'BH', name: '巴林', nameEn: 'Bahrain', template: 'modern' },
    { code: 'BD', name: '孟加拉国', nameEn: 'Bangladesh', template: 'pyramid' },
    { code: 'BB', name: '巴巴多斯', nameEn: 'Barbados', template: 'sphere' },
    { code: 'BY', name: '白俄罗斯', nameEn: 'Belarus', template: 'modern' },
    { code: 'BE', name: '比利时', nameEn: 'Belgium', template: 'modern' },
    { code: 'BZ', name: '伯利兹', nameEn: 'Belize', template: 'sphere' },
    { code: 'BJ', name: '贝宁', nameEn: 'Benin', template: 'pyramid' },
    { code: 'BT', name: '不丹', nameEn: 'Bhutan', template: 'pyramid' },
    { code: 'BO', name: '玻利维亚', nameEn: 'Bolivia', template: 'lattice' },
    { code: 'BA', name: '波黑', nameEn: 'Bosnia', template: 'modern' },
    { code: 'BW', name: '博茨瓦纳', nameEn: 'Botswana', template: 'modern' },
    { code: 'BR', name: '巴西', nameEn: 'Brazil', template: 'modern' },
    { code: 'BN', name: '文莱', nameEn: 'Brunei', template: 'sphere' },
    { code: 'BG', name: '保加利亚', nameEn: 'Bulgaria', template: 'modern' },
    { code: 'BF', name: '布基纳法索', nameEn: 'Burkina', template: 'pyramid' },
    { code: 'BI', name: '布隆迪', nameEn: 'Burundi', template: 'modern' },
    
    // C开头国家
    { code: 'CV', name: '佛得角', nameEn: 'Cape Verde', template: 'sphere' },
    { code: 'KH', name: '柬埔寨', nameEn: 'Cambodia', template: 'pyramid' },
    { code: 'CM', name: '喀麦隆', nameEn: 'Cameroon', template: 'modern' },
    { code: 'CA', name: '加拿大', nameEn: 'Canada', template: 'modern' },
    { code: 'CF', name: '中非', nameEn: 'CAR', template: 'pyramid' },
    { code: 'TD', name: '乍得', nameEn: 'Chad', template: 'pyramid' },
    { code: 'CL', name: '智利', nameEn: 'Chile', template: 'lattice' },
    { code: 'CN', name: '中国', nameEn: 'China', template: 'sphere', special: 'oriental-pearl' },
    { code: 'CO', name: '哥伦比亚', nameEn: 'Colombia', template: 'modern' },
    { code: 'KM', name: '科摩罗', nameEn: 'Comoros', template: 'sphere' },
    { code: 'CG', name: '刚果', nameEn: 'Congo', template: 'modern' },
    { code: 'CR', name: '哥斯达黎加', nameEn: 'Costa Rica', template: 'sphere' },
    { code: 'HR', name: '克罗地亚', nameEn: 'Croatia', template: 'modern' },
    { code: 'CU', name: '古巴', nameEn: 'Cuba', template: 'modern' },
    { code: 'CY', name: '塞浦路斯', nameEn: 'Cyprus', template: 'pyramid' },
    { code: 'CZ', name: '捷克', nameEn: 'Czech', template: 'modern' },
    { code: 'CI', name: '科特迪瓦', nameEn: 'Ivory Coast', template: 'modern' },
    
    // D开头国家
    { code: 'DK', name: '丹麦', nameEn: 'Denmark', template: 'modern' },
    { code: 'DJ', name: '吉布提', nameEn: 'Djibouti', template: 'modern' },
    { code: 'DM', name: '多米尼克', nameEn: 'Dominica', template: 'sphere' },
    { code: 'DO', name: '多米尼加', nameEn: 'Dominican', template: 'modern' },
    { code: 'CD', name: '刚果金', nameEn: 'DRC', template: 'modern' },
    
    // E开头国家
    { code: 'EC', name: '厄瓜多尔', nameEn: 'Ecuador', template: 'modern' },
    { code: 'EG', name: '埃及', nameEn: 'Egypt', template: 'pyramid', special: 'great-pyramid' },
    { code: 'SV', name: '萨尔瓦多', nameEn: 'El Salvador', template: 'modern' },
    { code: 'GQ', name: '赤道几内亚', nameEn: 'Equatorial Guinea', template: 'sphere' },
    { code: 'ER', name: '厄立特里亚', nameEn: 'Eritrea', template: 'modern' },
    { code: 'EE', name: '爱沙尼亚', nameEn: 'Estonia', template: 'modern' },
    { code: 'SZ', name: '斯威士兰', nameEn: 'Eswatini', template: 'modern' },
    { code: 'ET', name: '埃塞俄比亚', nameEn: 'Ethiopia', template: 'pyramid' },
    
    // F开头国家
    { code: 'FJ', name: '斐济', nameEn: 'Fiji', template: 'sphere' },
    { code: 'FI', name: '芬兰', nameEn: 'Finland', template: 'modern' },
    { code: 'FR', name: '法国', nameEn: 'France', template: 'lattice', special: 'eiffel-tower' },
    
    // G开头国家
    { code: 'GA', name: '加蓬', nameEn: 'Gabon', template: 'modern' },
    { code: 'GM', name: '冈比亚', nameEn: 'Gambia', template: 'sphere' },
    { code: 'GE', name: '格鲁吉亚', nameEn: 'Georgia', template: 'modern' },
    { code: 'DE', name: '德国', nameEn: 'Germany', template: 'modern' },
    { code: 'GH', name: '加纳', nameEn: 'Ghana', template: 'pyramid' },
    { code: 'GR', name: '希腊', nameEn: 'Greece', template: 'pyramid' },
    { code: 'GD', name: '格林纳达', nameEn: 'Grenada', template: 'sphere' },
    { code: 'GT', name: '危地马拉', nameEn: 'Guatemala', template: 'pyramid' },
    { code: 'GN', name: '几内亚', nameEn: 'Guinea', template: 'modern' },
    { code: 'GW', name: '几内亚比绍', nameEn: 'Guinea-Bissau', template: 'sphere' },
    { code: 'GY', name: '圭亚那', nameEn: 'Guyana', template: 'sphere' },
    
    // H开头国家
    { code: 'HT', name: '海地', nameEn: 'Haiti', template: 'modern' },
    { code: 'HN', name: '洪都拉斯', nameEn: 'Honduras', template: 'modern' },
    { code: 'HU', name: '匈牙利', nameEn: 'Hungary', template: 'modern' },
    
    // I开头国家
    { code: 'IS', name: '冰岛', nameEn: 'Iceland', template: 'modern' },
    { code: 'IN', name: '印度', nameEn: 'India', template: 'pyramid' },
    { code: 'ID', name: '印度尼西亚', nameEn: 'Indonesia', template: 'sphere' },
    { code: 'IR', name: '伊朗', nameEn: 'Iran', template: 'pyramid' },
    { code: 'IQ', name: '伊拉克', nameEn: 'Iraq', template: 'pyramid' },
    { code: 'IE', name: '爱尔兰', nameEn: 'Ireland', template: 'modern' },
    { code: 'IL', name: '以色列', nameEn: 'Israel', template: 'modern' },
    { code: 'IT', name: '意大利', nameEn: 'Italy', template: 'pyramid' },
    
    // J开头国家
    { code: 'JM', name: '牙买加', nameEn: 'Jamaica', template: 'sphere' },
    { code: 'JP', name: '日本', nameEn: 'Japan', template: 'sphere', special: 'tokyo-tower' },
    { code: 'JO', name: '约旦', nameEn: 'Jordan', template: 'pyramid' },
    
    // K开头国家
    { code: 'KZ', name: '哈萨克斯坦', nameEn: 'Kazakhstan', template: 'modern' },
    { code: 'KE', name: '肯尼亚', nameEn: 'Kenya', template: 'pyramid' },
    { code: 'KI', name: '基里巴斯', nameEn: 'Kiribati', template: 'sphere' },
    { code: 'KP', name: '朝鲜', nameEn: 'North Korea', template: 'modern' },
    { code: 'KR', name: '韩国', nameEn: 'South Korea', template: 'sphere' },
    { code: 'KW', name: '科威特', nameEn: 'Kuwait', template: 'modern' },
    { code: 'KG', name: '吉尔吉斯斯坦', nameEn: 'Kyrgyzstan', template: 'modern' },
    
    // L开头国家
    { code: 'LA', name: '老挝', nameEn: 'Laos', template: 'pyramid' },
    { code: 'LV', name: '拉脱维亚', nameEn: 'Latvia', template: 'modern' },
    { code: 'LB', name: '黎巴嫩', nameEn: 'Lebanon', template: 'pyramid' },
    { code: 'LS', name: '莱索托', nameEn: 'Lesotho', template: 'modern' },
    { code: 'LR', name: '利比里亚', nameEn: 'Liberia', template: 'modern' },
    { code: 'LY', name: '利比亚', nameEn: 'Libya', template: 'pyramid' },
    { code: 'LI', name: '列支敦士登', nameEn: 'Liechtenstein', template: 'modern' },
    { code: 'LT', name: '立陶宛', nameEn: 'Lithuania', template: 'modern' },
    { code: 'LU', name: '卢森堡', nameEn: 'Luxembourg', template: 'modern' },
    
    // M开头国家
    { code: 'MG', name: '马达加斯加', nameEn: 'Madagascar', template: 'sphere' },
    { code: 'MW', name: '马拉维', nameEn: 'Malawi', template: 'modern' },
    { code: 'MY', name: '马来西亚', nameEn: 'Malaysia', template: 'modern' },
    { code: 'MV', name: '马尔代夫', nameEn: 'Maldives', template: 'sphere' },
    { code: 'ML', name: '马里', nameEn: 'Mali', template: 'pyramid' },
    { code: 'MT', name: '马耳他', nameEn: 'Malta', template: 'pyramid' },
    { code: 'MH', name: '马绍尔', nameEn: 'Marshall', template: 'sphere' },
    { code: 'MR', name: '毛里塔尼亚', nameEn: 'Mauritania', template: 'pyramid' },
    { code: 'MU', name: '毛里求斯', nameEn: 'Mauritius', template: 'sphere' },
    { code: 'MX', name: '墨西哥', nameEn: 'Mexico', template: 'pyramid' },
    { code: 'FM', name: '密克罗尼西亚', nameEn: 'Micronesia', template: 'sphere' },
    { code: 'MD', name: '摩尔多瓦', nameEn: 'Moldova', template: 'modern' },
    { code: 'MC', name: '摩纳哥', nameEn: 'Monaco', template: 'modern' },
    { code: 'MN', name: '蒙古', nameEn: 'Mongolia', template: 'modern' },
    { code: 'ME', name: '黑山', nameEn: 'Montenegro', template: 'modern' },
    { code: 'MA', name: '摩洛哥', nameEn: 'Morocco', template: 'pyramid' },
    { code: 'MZ', name: '莫桑比克', nameEn: 'Mozambique', template: 'modern' },
    { code: 'MM', name: '缅甸', nameEn: 'Myanmar', template: 'pyramid' },
    
    // N开头国家
    { code: 'NA', name: '纳米比亚', nameEn: 'Namibia', template: 'modern' },
    { code: 'NR', name: '瑙鲁', nameEn: 'Nauru', template: 'sphere' },
    { code: 'NP', name: '尼泊尔', nameEn: 'Nepal', template: 'pyramid' },
    { code: 'NL', name: '荷兰', nameEn: 'Netherlands', template: 'modern' },
    { code: 'NZ', name: '新西兰', nameEn: 'New Zealand', template: 'sphere' },
    { code: 'NI', name: '尼加拉瓜', nameEn: 'Nicaragua', template: 'modern' },
    { code: 'NE', name: '尼日尔', nameEn: 'Niger', template: 'pyramid' },
    { code: 'NG', name: '尼日利亚', nameEn: 'Nigeria', template: 'modern' },
    { code: 'MK', name: '北马其顿', nameEn: 'North Macedonia', template: 'modern' },
    { code: 'NO', name: '挪威', nameEn: 'Norway', template: 'modern' },
    
    // O开头国家
    { code: 'OM', name: '阿曼', nameEn: 'Oman', template: 'modern' },
    
    // P开头国家
    { code: 'PK', name: '巴基斯坦', nameEn: 'Pakistan', template: 'modern' },
    { code: 'PW', name: '帕劳', nameEn: 'Palau', template: 'sphere' },
    { code: 'PA', name: '巴拿马', nameEn: 'Panama', template: 'modern' },
    { code: 'PG', name: '巴布亚新几内亚', nameEn: 'PNG', template: 'sphere' },
    { code: 'PY', name: '巴拉圭', nameEn: 'Paraguay', template: 'modern' },
    { code: 'PE', name: '秘鲁', nameEn: 'Peru', template: 'pyramid' },
    { code: 'PH', name: '菲律宾', nameEn: 'Philippines', template: 'modern' },
    { code: 'PL', name: '波兰', nameEn: 'Poland', template: 'modern' },
    { code: 'PT', name: '葡萄牙', nameEn: 'Portugal', template: 'modern' },
    
    // Q开头国家
    { code: 'QA', name: '卡塔尔', nameEn: 'Qatar', template: 'modern' },
    
    // R开头国家
    { code: 'RO', name: '罗马尼亚', nameEn: 'Romania', template: 'modern' },
    { code: 'RU', name: '俄罗斯', nameEn: 'Russia', template: 'lattice' },
    { code: 'RW', name: '卢旺达', nameEn: 'Rwanda', template: 'modern' },
    
    // S开头国家
    { code: 'KN', name: '圣基茨', nameEn: 'Saint Kitts', template: 'sphere' },
    { code: 'LC', name: '圣卢西亚', nameEn: 'Saint Lucia', template: 'sphere' },
    { code: 'VC', name: '圣文森特', nameEn: 'Saint Vincent', template: 'sphere' },
    { code: 'WS', name: '萨摩亚', nameEn: 'Samoa', template: 'sphere' },
    { code: 'SM', name: '圣马力诺', nameEn: 'San Marino', template: 'modern' },
    { code: 'ST', name: '圣多美', nameEn: 'Sao Tome', template: 'sphere' },
    { code: 'SA', name: '沙特', nameEn: 'Saudi Arabia', template: 'modern' },
    { code: 'SN', name: '塞内加尔', nameEn: 'Senegal', template: 'pyramid' },
    { code: 'RS', name: '塞尔维亚', nameEn: 'Serbia', template: 'modern' },
    { code: 'SC', name: '塞舌尔', nameEn: 'Seychelles', template: 'sphere' },
    { code: 'SL', name: '塞拉利昂', nameEn: 'Sierra Leone', template: 'modern' },
    { code: 'SG', name: '新加坡', nameEn: 'Singapore', template: 'sphere' },
    { code: 'SK', name: '斯洛伐克', nameEn: 'Slovakia', template: 'modern' },
    { code: 'SI', name: '斯洛文尼亚', nameEn: 'Slovenia', template: 'modern' },
    { code: 'SB', name: '所罗门群岛', nameEn: 'Solomon', template: 'sphere' },
    { code: 'SO', name: '索马里', nameEn: 'Somalia', template: 'modern' },
    { code: 'ZA', name: '南非', nameEn: 'South Africa', template: 'modern' },
    { code: 'SS', name: '南苏丹', nameEn: 'South Sudan', template: 'modern' },
    { code: 'ES', name: '西班牙', nameEn: 'Spain', template: 'modern' },
    { code: 'LK', name: '斯里兰卡', nameEn: 'Sri Lanka', template: 'pyramid' },
    { code: 'SD', name: '苏丹', nameEn: 'Sudan', template: 'pyramid' },
    { code: 'SR', name: '苏里南', nameEn: 'Suriname', template: 'sphere' },
    { code: 'SE', name: '瑞典', nameEn: 'Sweden', template: 'modern' },
    { code: 'CH', name: '瑞士', nameEn: 'Switzerland', template: 'modern' },
    { code: 'SY', name: '叙利亚', nameEn: 'Syria', template: 'pyramid' },
    
    // T开头国家
    { code: 'TJ', name: '塔吉克斯坦', nameEn: 'Tajikistan', template: 'modern' },
    { code: 'TZ', name: '坦桑尼亚', nameEn: 'Tanzania', template: 'modern' },
    { code: 'TH', name: '泰国', nameEn: 'Thailand', template: 'pyramid' },
    { code: 'TL', name: '东帝汶', nameEn: 'Timor-Leste', template: 'sphere' },
    { code: 'TG', name: '多哥', nameEn: 'Togo', template: 'modern' },
    { code: 'TO', name: '汤加', nameEn: 'Tonga', template: 'sphere' },
    { code: 'TT', name: '特立尼达', nameEn: 'Trinidad', template: 'sphere' },
    { code: 'TN', name: '突尼斯', nameEn: 'Tunisia', template: 'pyramid' },
    { code: 'TR', name: '土耳其', nameEn: 'Turkey', template: 'modern' },
    { code: 'TM', name: '土库曼斯坦', nameEn: 'Turkmenistan', template: 'modern' },
    { code: 'TV', name: '图瓦卢', nameEn: 'Tuvalu', template: 'sphere' },
    
    // U开头国家
    { code: 'UG', name: '乌干达', nameEn: 'Uganda', template: 'modern' },
    { code: 'UA', name: '乌克兰', nameEn: 'Ukraine', template: 'lattice' },
    { code: 'AE', name: '阿联酋', nameEn: 'UAE', template: 'modern' },
    { code: 'GB', name: '英国', nameEn: 'UK', template: 'lattice' },
    { code: 'US', name: '美国', nameEn: 'USA', template: 'modern' },
    { code: 'UY', name: '乌拉圭', nameEn: 'Uruguay', template: 'modern' },
    { code: 'UZ', name: '乌兹别克斯坦', nameEn: 'Uzbekistan', template: 'pyramid' },
    
    // V开头国家
    { code: 'VU', name: '瓦努阿图', nameEn: 'Vanuatu', template: 'sphere' },
    { code: 'VA', name: '梵蒂冈', nameEn: 'Vatican', template: 'pyramid' },
    { code: 'VE', name: '委内瑞拉', nameEn: 'Venezuela', template: 'modern' },
    { code: 'VN', name: '越南', nameEn: 'Vietnam', template: 'pyramid' },
    
    // Y开头国家
    { code: 'YE', name: '也门', nameEn: 'Yemen', template: 'pyramid' },
    
    // Z开头国家
    { code: 'ZM', name: '赞比亚', nameEn: 'Zambia', template: 'modern' },
    { code: 'ZW', name: '津巴布韦', nameEn: 'Zimbabwe', template: 'modern' }
];

/**
 * 生成196个塔的完整配置
 */
export function generateAllTowerConfigs() {
    const configs = {};

    COUNTRY_TOWERS.forEach(country => {
        const towerId = `tower-${country.code.toLowerCase()}`;
        const template = TEMPLATES[country.template];
        
        if (template) {
            configs[towerId] = {
                id: towerId,
                code: country.code,
                name: country.name,
                nameEn: country.nameEn,
                template: country.template,
                special: country.special || null,
                layers: template.generateLayers(),
                style: template.type
            };
        }
    });

    return configs;
}

/**
 * 获取单个塔配置
 */
export function getTowerConfig(towerId) {
    const configs = generateAllTowerConfigs();
    return configs[towerId] || null;
}

/**
 * 根据模板类型获取塔列表
 */
export function getTowersByTemplate(templateType) {
    const configs = generateAllTowerConfigs();
    return Object.values(configs).filter(config => config.template === templateType);
}

/**
 * 196个塔配置数据
 */
export const TOWER_3D_CONFIGS = generateAllTowerConfigs();

export default TOWER_3D_CONFIGS;
