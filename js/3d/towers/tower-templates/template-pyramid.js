/**
 * 金字塔模板 - 埃及风格类
 * 特点：四棱锥结构，古老神秘
 */

export const PyramidTowerTemplate = {
    type: 'pyramid',
    name: '金字塔塔',
    description: '古老的金字塔结构，象征力量与永恒',
    
    generateLayers() {
        const layers = [];
        const layerNames = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
        
        // 金字塔逐层收窄（从顶部开始）
        const baseSizes = [0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 4.5, 5.0];
        const heights = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 1.0];
        const yPositions = [5.5, 5.0, 4.4, 3.8, 3.15, 2.45, 1.7, 0.9, 0.05, -0.85, -1.8, -2.8, -3.9];
        
        // 颜色渐变 - 从金色到沙色
        const colors = [
            0xFFD700, 0xFFC800, 0xFFB900, 0xFFAA00, 0xFF9B00,
            0xFFB347, 0xFFAE42, 0xD4AF37, 0xC5B358, 0xB5A642,
            0xC19A6B, 0xE6C288, 0xF4A460
        ];
        
        for (let i = 0; i < 13; i++) {
            layers.push({
                type: 'box',
                width: baseSizes[i],
                height: heights[i],
                depth: baseSizes[i],
                y: yPositions[i],
                color: colors[i],
                emissive: 0x221100,
                style: 'pyramid',
                layerIndex: i,
                layerName: layerNames[i],
                playerPositions: this.generatePlayerPositions(i, baseSizes[i]),
                guardPositions: this.generateGuardPositions(i, baseSizes[i])
            });
        }
        
        return layers;
    },

    generatePlayerPositions(layerIndex, size) {
        const baseY = 5.5 - (layerIndex * 0.45);
        const offset = size * 0.35;
        
        return [
            { x: offset, y: baseY, z: 0, direction: 'east', index: 0 },
            { x: 0, y: baseY, z: offset, direction: 'south', index: 1 },
            { x: -offset, y: baseY, z: 0, direction: 'west', index: 2 },
            { x: 0, y: baseY, z: -offset, direction: 'north', index: 3 }
        ];
    },

    generateGuardPositions(layerIndex, size) {
        const positions = [];
        const baseY = 5.5 - (layerIndex * 0.45) + 0.15;
        const offset = size * 0.5;
        const count = 4;
        
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.PI / 4);
            positions.push({
                x: Math.cos(angle) * offset,
                y: baseY,
                z: Math.sin(angle) * offset,
                angle: angle,
                index: i
            });
        }
        
        return positions;
    },

    materials: {
        gold: { color: 0xFFD700, emissive: 0x443300, shininess: 100 },
        sand: { color: 0xF4A460, emissive: 0x221100, shininess: 30 },
        stone: { color: 0xC19A6B, emissive: 0x1a1005, shininess: 20 }
    }
};

export default PyramidTowerTemplate;
