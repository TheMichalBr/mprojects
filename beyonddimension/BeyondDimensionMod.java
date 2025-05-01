import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.level.dimension.DimensionType;
import net.minecraft.world.level.dimension.LevelStem;
import net.minecraft.world.level.levelgen.presets.WorldPresets;
import net.minecraft.world.level.levelgen.structure.templatesystem.StructureTemplateManager;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

package com.example.beyonddimension;


@Mod("beyonddimension")
public class BeyondDimensionMod {
    public static final String MOD_ID = "beyonddimension";

    public BeyondDimensionMod() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();

        modEventBus.addListener(this::commonSetup);

        MinecraftForge.EVENT_BUS.register(this);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        // Zde můžete inicializovat věci, jako je registrace dimenzí
    }

    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event) {
        // Zde můžete přidat logiku, která se spustí při startu serveru
    }

    public static ResourceKey<LevelStem> createDimensionKey(String name) {
        return ResourceKey.create(Registries.LEVEL_STEM, new ResourceLocation(MOD_ID, name));
    }

    public static ResourceKey<DimensionType> createDimensionTypeKey(String name) {
        return ResourceKey.create(Registries.DIMENSION_TYPE, new ResourceLocation(MOD_ID, name));
    }
}