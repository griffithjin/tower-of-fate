/**
 * Allegro 3D Towers - 196个国家塔模型系统
 * 主入口文件
 */

// 导出3D塔生成器
export { Tower3DGenerator } from './tower-generator.js';

// 导出196个塔配置
export { 
    TOWER_3D_CONFIGS, 
    generateAllTowerConfigs, 
    getTowerConfig,
    getTowersByTemplate 
} from './tower-configs-3d.js';

// 导出模板
export { SphereTowerTemplate } from './tower-templates/template-sphere.js';
export { LatticeTowerTemplate } from './tower-templates/template-lattice.js';
export { PyramidTowerTemplate } from './tower-templates/template-pyramid.js';
export { ModernTowerTemplate } from './tower-templates/template-modern.js';

// 版本信息
export const VERSION = '1.0.0';
export const TOWER_COUNT = 196;
export const LAYER_COUNT = 13;

/**
 * Allegro3DTowers - 主类
 * 提供简洁的API来生成和管理196个3D塔
 */
export class Allegro3DTowers {
    constructor() {
        this.generator = null;
        this.configs = null;
        this.initialized = false;
    }

    /**
     * 初始化系统
     * @param {Object} options - 配置选项
     */
    async init(options = {}) {
        // 动态导入Three.js（如果环境中没有）
        if (typeof THREE === 'undefined') {
            const THREE_MODULE = await import('three');
            window.THREE = THREE_MODULE;
        }

        const { Tower3DGenerator } = await import('./tower-generator.js');
        const { generateAllTowerConfigs } = await import('./tower-configs-3d.js');

        this.generator = new Tower3DGenerator();
        this.configs = generateAllTowerConfigs();
        this.initialized = true;

        console.log(`🗼 Allegro 3D Towers 初始化完成！共 ${TOWER_COUNT} 个塔模型`);
        return this;
    }

    /**
     * 生成单个塔模型
     * @param {string} towerId - 塔ID (如 'tower-cn')
     * @returns {THREE.Group} 塔3D模型
     */
    generateTower(towerId) {
        if (!this.initialized) {
            throw new Error('请先调用 init() 初始化系统');
        }

        const config = this.configs[towerId];
        if (!config) {
            console.error(`塔 ${towerId} 不存在`);
            return null;
        }

        return this.generator.generateTower3D(config);
    }

    /**
     * 生成所有塔模型
     * @returns {Object} 塔模型映射 {towerId: THREE.Group}
     */
    generateAllTowers() {
        if (!this.initialized) {
            throw new Error('请先调用 init() 初始化系统');
        }

        const towers = {};
        Object.keys(this.configs).forEach(towerId => {
            towers[towerId] = this.generateTower(towerId);
        });

        return towers;
    }

    /**
     * 获取塔配置
     * @param {string} towerId - 塔ID
     * @returns {Object} 塔配置
     */
    getConfig(towerId) {
        return this.configs?.[towerId] || null;
    }

    /**
     * 获取所有塔配置
     * @returns {Object} 所有塔配置
     */
    getAllConfigs() {
        return this.configs;
    }

    /**
     * 按模板类型获取塔
     * @param {string} templateType - 模板类型 (sphere/lattice/pyramid/modern)
     * @returns {Array} 塔配置数组
     */
    getTowersByTemplate(templateType) {
        return Object.values(this.configs).filter(
            config => config.template === templateType
        );
    }

    /**
     * 更新玩家头像
     * @param {THREE.Group} tower - 塔模型
     * @param {number} layerIndex - 层索引 (0-12)
     * @param {number} playerIndex - 玩家索引 (0-3)
     * @param {string} avatarUrl - 头像URL
     */
    updatePlayerAvatar(tower, layerIndex, playerIndex, avatarUrl) {
        if (this.generator) {
            this.generator.updatePlayerAvatar(tower, layerIndex, playerIndex, avatarUrl);
        }
    }

    /**
     * 获取统计信息
     */
    getStats() {
        if (!this.configs) return null;

        const configs = Object.values(this.configs);
        const templateCounts = {
            sphere: configs.filter(c => c.template === 'sphere').length,
            lattice: configs.filter(c => c.template === 'lattice').length,
            pyramid: configs.filter(c => c.template === 'pyramid').length,
            modern: configs.filter(c => c.template === 'modern').length
        };

        return {
            totalTowers: configs.length,
            totalLayers: configs.length * LAYER_COUNT,
            templateDistribution: templateCounts,
            version: VERSION
        };
    }
}

// 默认导出
export default Allegro3DTowers;

// 全局访问（浏览器环境）
if (typeof window !== 'undefined') {
    window.Allegro3DTowers = Allegro3DTowers;
}
