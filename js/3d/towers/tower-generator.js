/**
 * Tower3DGenerator - 3D塔程序化生成器
 * 基于Three.js的196个塔模型生成系统
 */

import * as THREE from 'three';

export class Tower3DGenerator {
    constructor() {
        this.textureLoader = new THREE.TextureLoader();
        this.materialCache = new Map();
    }

    /**
     * 生成3D塔模型
     * @param {Object} config - 塔配置
     * @returns {THREE.Group} 塔3D模型组
     */
    generateTower3D(config) {
        const towerGroup = new THREE.Group();
        towerGroup.name = `tower-${config.id}`;

        // 生成13层
        config.layers.forEach((layerConfig, i) => {
            const layer = this.createLayer3D(layerConfig, i);
            towerGroup.add(layer);

            // 添加玩家位置标记
            const playerMarkers = this.createPlayerPositionMarkers(layerConfig);
            towerGroup.add(playerMarkers);

            // 添加守卫位置标记
            const guardMarkers = this.createGuardPositionMarkers(layerConfig);
            towerGroup.add(guardMarkers);
        });

        // 添加整体光效
        this.addTowerEffects(towerGroup, config);

        return towerGroup;
    }

    /**
     * 创建单个层
     */
    createLayer3D(config, layerIndex) {
        let geometry, material;

        switch (config.type) {
            case 'sphere':
                geometry = new THREE.SphereGeometry(config.radius || 1, 32, 16);
                break;
            case 'cylinder':
                geometry = new THREE.CylinderGeometry(
                    config.radius || 0.5,
                    config.radius || 0.5,
                    config.height || 1,
                    32
                );
                break;
            case 'platform':
                geometry = new THREE.CylinderGeometry(
                    config.width || 2,
                    (config.width || 2) * 0.9,
                    config.height || 0.3,
                    6
                );
                break;
            case 'box':
                geometry = new THREE.BoxGeometry(
                    config.width || 1,
                    config.height || 0.5,
                    config.depth || 1
                );
                break;
            default:
                geometry = new THREE.CylinderGeometry(1, 1, 0.5, 32);
        }

        // 创建材质（带缓存）
        const materialKey = `${config.color}-${config.emissive}-${config.style}`;
        if (this.materialCache.has(materialKey)) {
            material = this.materialCache.get(materialKey);
        } else {
            material = new THREE.MeshPhongMaterial({
                color: config.color || this.getLayerColor(layerIndex),
                emissive: config.emissive || 0x000000,
                transparent: true,
                opacity: config.opacity || 0.9,
                shininess: config.shininess || 100,
                side: THREE.DoubleSide
            });
            this.materialCache.set(materialKey, material);
        }

        const mesh = new THREE.Mesh(geometry, material);
        mesh.position.y = config.y !== undefined ? config.y : layerIndex * 0.5;
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        mesh.name = `layer-${config.layerName || layerIndex}`;

        // 添加层标识
        const label = this.createLayerLabel(config.layerName || layerIndex);
        label.position.y = mesh.position.y + (config.height || 0.5) / 2 + 0.1;
        mesh.add(label);

        return mesh;
    }

    /**
     * 创建层标识
     */
    createLayerLabel(layerName) {
        const canvas = document.createElement('canvas');
        canvas.width = 64;
        canvas.height = 64;
        const ctx = canvas.getContext('2d');

        // 绘制背景
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.beginPath();
        ctx.arc(32, 32, 30, 0, Math.PI * 2);
        ctx.fill();

        // 绘制文字
        ctx.fillStyle = '#FFD700';
        ctx.font = 'bold 36px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(String(layerName), 32, 32);

        const texture = new THREE.CanvasTexture(canvas);
        const spriteMaterial = new THREE.SpriteMaterial({ map: texture });
        const sprite = new THREE.Sprite(spriteMaterial);
        sprite.scale.set(0.5, 0.5, 1);

        return sprite;
    }

    /**
     * 创建玩家位置标记
     */
    createPlayerPositionMarkers(layerConfig) {
        const group = new THREE.Group();
        group.name = `players-layer-${layerConfig.layerName}`;

        const positions = layerConfig.playerPositions || [];

        positions.forEach((pos, i) => {
            // 头像底座
            const baseGeometry = new THREE.CylinderGeometry(0.15, 0.15, 0.05, 16);
            const baseMaterial = new THREE.MeshPhongMaterial({
                color: 0xffd700,
                emissive: 0x332200,
                shininess: 100
            });
            const base = new THREE.Mesh(baseGeometry, baseMaterial);
            base.position.set(pos.x, pos.y, pos.z);
            base.name = `player-base-${i}`;

            // 头像展示平面（占位符，实际使用时加载真实头像）
            const planeGeometry = new THREE.PlaneGeometry(0.25, 0.25);
            const planeMaterial = new THREE.MeshBasicMaterial({
                color: 0x444444,
                transparent: true,
                opacity: 0.8,
                side: THREE.DoubleSide
            });
            const avatarPlane = new THREE.Mesh(planeGeometry, planeMaterial);
            avatarPlane.position.set(pos.x, pos.y + 0.15, pos.z);
            avatarPlane.lookAt(0, pos.y + 0.15, 0);
            avatarPlane.name = `player-avatar-${i}`;

            // 玩家编号
            const label = this.createPlayerLabel(i + 1);
            label.position.set(pos.x, pos.y + 0.35, pos.z);

            group.add(base);
            group.add(avatarPlane);
            group.add(label);
        });

        return group;
    }

    /**
     * 创建玩家编号标签
     */
    createPlayerLabel(playerIndex) {
        const canvas = document.createElement('canvas');
        canvas.width = 32;
        canvas.height = 32;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = '#00ff00';
        ctx.font = 'bold 20px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(String(playerIndex), 16, 16);

        const texture = new THREE.CanvasTexture(canvas);
        const spriteMaterial = new THREE.SpriteMaterial({ map: texture });
        const sprite = new THREE.Sprite(spriteMaterial);
        sprite.scale.set(0.3, 0.3, 1);

        return sprite;
    }

    /**
     * 创建守卫位置标记
     */
    createGuardPositionMarkers(layerConfig) {
        const group = new THREE.Group();
        group.name = `guards-layer-${layerConfig.layerName}`;

        const positions = layerConfig.guardPositions || [];

        positions.forEach((pos, i) => {
            // 守卫标记
            const geometry = new THREE.OctahedronGeometry(0.08, 0);
            const material = new THREE.MeshPhongMaterial({
                color: 0xff0000,
                emissive: 0x330000,
                shininess: 80
            });
            const guard = new THREE.Mesh(geometry, material);
            guard.position.set(pos.x, pos.y, pos.z);
            guard.name = `guard-${i}`;

            // 守卫光环
            const ringGeometry = new THREE.RingGeometry(0.1, 0.12, 16);
            const ringMaterial = new THREE.MeshBasicMaterial({
                color: 0xff0000,
                transparent: true,
                opacity: 0.5,
                side: THREE.DoubleSide
            });
            const ring = new THREE.Mesh(ringGeometry, ringMaterial);
            ring.position.set(pos.x, pos.y - 0.1, pos.z);
            ring.rotation.x = -Math.PI / 2;

            group.add(guard);
            group.add(ring);
        });

        return group;
    }

    /**
     * 添加塔的整体特效
     */
    addTowerEffects(towerGroup, config) {
        // 添加塔顶光芒
        const topLight = new THREE.PointLight(
            config.topLightColor || 0xffd700,
            1,
            10
        );
        topLight.position.set(0, 7, 0);
        topLight.name = 'top-light';
        towerGroup.add(topLight);

        // 添加环境光
        const ambientLight = new THREE.AmbientLight(0x404040, 0.5);
        towerGroup.add(ambientLight);
    }

    /**
     * 获取层颜色（默认渐变）
     */
    getLayerColor(layerIndex) {
        const colors = [
            0xff1493, 0xff69b4, 0xffa500, 0xffff00, 0x00ff00,
            0x00ffff, 0x0000ff, 0x8b00ff, 0xff00ff, 0xff1493,
            0xff6347, 0xff4500, 0xdc143c
        ];
        return colors[layerIndex % colors.length];
    }

    /**
     * 更新玩家头像
     */
    updatePlayerAvatar(towerGroup, layerIndex, playerIndex, avatarUrl) {
        const playerGroup = towerGroup.getObjectByName(`players-layer-${this.getLayerName(layerIndex)}`);
        if (!playerGroup) return;

        const avatarMesh = playerGroup.getObjectByName(`player-avatar-${playerIndex}`);
        if (!avatarMesh) return;

        this.textureLoader.load(avatarUrl, (texture) => {
            avatarMesh.material.map = texture;
            avatarMesh.material.needsUpdate = true;
        });
    }

    /**
     * 获取层名称
     */
    getLayerName(layerIndex) {
        const names = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'];
        return names[layerIndex] || layerIndex;
    }
}

export default Tower3DGenerator;
