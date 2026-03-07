/**
 * 铁架塔模板 - 埃菲尔铁塔类
 * 特点：镂空铁架结构，逐层收窄
 */

export const LatticeTowerTemplate = {
    type: 'lattice',
    name: '铁架塔',
    description: '经典镂空铁架结构，工业美学典范',
    
    generateLayers() {
        const layers = [];
        const layerNames = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
        
        // 埃菲尔式逐层收窄
        const widths = [1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.8, 3.1, 3.4, 3.8, 4.2, 4.6, 5.0];
        const heights = [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.8];
        const yPositions = [6, 5.5, 5, 4.4, 3.8, 3.2, 2.6, 2, 1.4, 0.8, 0.2, -0.4, -1.1];
        
        widths.reverse(); // 从底层到顶层收窄
        
        for (let i = 0; i < 13; i++) {
            const isTop = i < 3;
            layers.push({
                type: 'platform',
                width: widths[i],
                height: heights[i],
                depth: widths[i],
                y: yPositions[i],
                color: isTop ? 0x8B4513 : 0x4a4a4a, // 顶部铜色，底部铁色
                emissive: isTop ? 0x331100 : 0x111111,
                style: 'lattice',
                layerIndex: i,
                layerName: layerNames[i],
                playerPositions: this.generatePlayerPositions(i, widths[i]),
                guardPositions: this.generateGuardPositions(i, widths[i])
            });
        }
        
        return layers;
    },

    generatePlayerPositions(layerIndex, width) {
        const baseY = 6 - (layerIndex * 0.5);
        const radius = width * 0.4;
        
        return [
            { x: radius, y: baseY, z: 0, direction: 'east', index: 0 },
            { x: 0, y: baseY, z: radius, direction: 'south', index: 1 },
            { x: -radius, y: baseY, z: 0, direction: 'west', index: 2 },
            { x: 0, y: baseY, z: -radius, direction: 'north', index: 3 }
        ];
    },

    generateGuardPositions(layerIndex, width) {
        const positions = [];
        const baseY = 6 - (layerIndex * 0.5) + 0.2;
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
        iron: { color: 0x4a4a4a, emissive: 0x111111, shininess: 60 },
        copper: { color: 0x8B4513, emissive: 0x331100, shininess: 80 },
        platform: { color: 0x696969, emissive: 0x000000, shininess: 40 }
    }
};

export default LatticeTowerTemplate;
