/**
 * 球体塔模板 - 东方明珠类
 * 特点：球体+圆柱体组合结构
 */

export const SphereTowerTemplate = {
    type: 'sphere',
    name: '球体塔',
    description: '多球体组合结构，具有现代感和科幻风格',
    
    // 层配置生成器
    generateLayers() {
        const layers = [];
        const layerConfigs = [
            { type: 'sphere', radius: 1.2, height: 0, y: 6, color: 0xff69b4 },      // A层 - 顶层球
            { type: 'cylinder', radius: 0.3, height: 1.5, y: 4.8, color: 0xff1493 }, // K层 - 连接柱
            { type: 'sphere', radius: 0.8, height: 0, y: 3.5, color: 0xff69b4 },    // Q层 - 中球
            { type: 'cylinder', radius: 0.4, height: 1.2, y: 2.5, color: 0xff1493 }, // J层 - 连接
            { type: 'sphere', radius: 1.5, height: 0, y: 1, color: 0xff69b4 },      // 10层 - 下大球
            { type: 'cylinder', radius: 0.6, height: 0.8, y: 0, color: 0xc0c0c0 },  // 9层 - 底座柱
            { type: 'cylinder', radius: 1.8, height: 0.3, y: -0.5, color: 0x808080 }, // 8层 - 底座
            { type: 'box', width: 1.5, height: 0.4, depth: 1.5, y: -0.9, color: 0x696969 }, // 7层
            { type: 'cylinder', radius: 1.2, height: 0.3, y: -1.3, color: 0x808080 }, // 6层
            { type: 'box', width: 2, height: 0.3, depth: 2, y: -1.7, color: 0x696969 }, // 5层
            { type: 'cylinder', radius: 2.2, height: 0.25, y: -2.1, color: 0x808080 }, // 4层
            { type: 'box', width: 2.5, height: 0.2, depth: 2.5, y: -2.4, color: 0x696969 }, // 3层
            { type: 'cylinder', radius: 2.8, height: 0.2, y: -2.7, color: 0x808080 }, // 2层
        ];

        const layerNames = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
        
        layerConfigs.forEach((config, i) => {
            layers.push({
                ...config,
                layerIndex: i,
                layerName: layerNames[i],
                playerPositions: this.generatePlayerPositions(i),
                guardPositions: this.generateGuardPositions(i)
            });
        });
        
        return layers;
    },

    // 生成玩家位置（每层4个方位）
    generatePlayerPositions(layerIndex) {
        const baseY = layerIndex * 0.5 + 0.3;
        const radius = 1.2 + (layerIndex * 0.1);
        
        return [
            { x: radius, y: baseY, z: 0, direction: 'east', index: 0 },      // 东
            { x: 0, y: baseY, z: radius, direction: 'south', index: 1 },     // 南
            { x: -radius, y: baseY, z: 0, direction: 'west', index: 2 },     // 西
            { x: 0, y: baseY, z: -radius, direction: 'north', index: 3 }     // 北
        ];
    },

    // 生成守卫位置
    generateGuardPositions(layerIndex) {
        const positions = [];
        const baseY = layerIndex * 0.5 + 0.5;
        const radius = 1.5 + (layerIndex * 0.15);
        const count = 4; // 每层4个守卫
        
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.PI / 4); // 45度偏移
            positions.push({
                x: Math.cos(angle) * radius,
                y: baseY,
                z: Math.sin(angle) * radius,
                angle: angle,
                index: i
            });
        }
        
        return positions;
    },

    // 材质配置
    materials: {
        primary: { color: 0xff69b4, emissive: 0x330033, shininess: 100 },
        secondary: { color: 0xff1493, emissive: 0x220022, shininess: 80 },
        base: { color: 0xc0c0c0, emissive: 0x111111, shininess: 60 },
        platform: { color: 0x808080, emissive: 0x000000, shininess: 40 }
    }
};

export default SphereTowerTemplate;
