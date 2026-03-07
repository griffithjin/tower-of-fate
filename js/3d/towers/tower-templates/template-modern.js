/**
 * 现代塔模板 - 摩天大楼类
 * 特点：玻璃幕墙，简洁现代
 */

export const ModernTowerTemplate = {
    type: 'modern',
    name: '现代塔',
    description: '玻璃幕墙摩天大楼，现代都市风格',
    
    generateLayers() {
        const layers = [];
        const layerNames = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
        
        // 现代塔配置 - 分段式结构
        const sections = [
            { levels: 3, width: 1.2, color: 0x00BFFF, emissive: 0x001133 }, // 顶部 - 亮蓝
            { levels: 4, width: 1.8, color: 0x1E90FF, emissive: 0x001a33 }, // 上部
            { levels: 3, width: 2.4, color: 0x4169E1, emissive: 0x002244 }, // 中部
            { levels: 3, width: 3.0, color: 0x0000CD, emissive: 0x001133 }  // 底部
        ];
        
        let currentLayer = 0;
        let currentY = 5.5;
        
        sections.forEach(section => {
            for (let i = 0; i < section.levels && currentLayer < 13; i++) {
                layers.push({
                    type: 'box',
                    width: section.width,
                    height: 0.5,
                    depth: section.width,
                    y: currentY,
                    color: section.color,
                    emissive: section.emissive,
                    style: 'modern',
                    layerIndex: currentLayer,
                    layerName: layerNames[currentLayer],
                    playerPositions: this.generatePlayerPositions(currentLayer, section.width),
                    guardPositions: this.generateGuardPositions(currentLayer, section.width)
                });
                
                currentY -= 0.6;
                currentLayer++;
            }
        });
        
        return layers;
    },

    generatePlayerPositions(layerIndex, width) {
        const baseY = 5.5 - (layerIndex * 0.5);
        const offset = width * 0.4;
        
        return [
            { x: offset, y: baseY, z: 0, direction: 'east', index: 0 },
            { x: 0, y: baseY, z: offset, direction: 'south', index: 1 },
            { x: -offset, y: baseY, z: 0, direction: 'west', index: 2 },
            { x: 0, y: baseY, z: -offset, direction: 'north', index: 3 }
        ];
    },

    generateGuardPositions(layerIndex, width) {
        const positions = [];
        const baseY = 5.5 - (layerIndex * 0.5) + 0.25;
        const radius = width * 0.55;
        const count = 4;
        
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2 + (Math.PI / 4);
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

    materials: {
        glass: { color: 0x00BFFF, emissive: 0x001133, shininess: 100, transparent: true, opacity: 0.9 },
        steel: { color: 0xC0C0C0, emissive: 0x111111, shininess: 80 },
        dark: { color: 0x2F4F4F, emissive: 0x051111, shininess: 60 }
    }
};

export default ModernTowerTemplate;
